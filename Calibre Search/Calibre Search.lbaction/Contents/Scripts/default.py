#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys
import json
import sqlite3
import subprocess
import re

class Concatenate():
    def __init__(self):
        self.itemList = []

    def step(self, value):
        # print 'step(%r)' % value
        self.itemList.append(value)

    def finalize(self):
        # print("final: %r" % ",".join(self.itemList))
        return "!@#$".join(self.itemList)

queryStr = sys.argv[1]
libraryPath = subprocess.check_output('/Applications/calibre.app/Contents/MacOS/calibre-debug -c "from calibre.utils.config import prefs; print(prefs.get(\'library_path\'),end=\'\')"', shell=True)

libraryPath = libraryPath.decode('utf-8')

metaDbPath = os.path.join(libraryPath, 'metadata.db')
con = sqlite3.connect(metaDbPath)
con.create_aggregate("concat", 1, Concatenate)
cur = con.cursor()
querySQL = """
SELECT id, title,
   (SELECT concat(name) FROM books_authors_link AS bal JOIN authors ON(author = authors.id) WHERE book = books.id) authors,
   (SELECT MAX(uncompressed_size) FROM data WHERE book=books.id) size,
   (SELECT concat(name) FROM tags WHERE tags.id IN (SELECT tag from books_tags_link WHERE book=books.id)) tags,
   (SELECT concat(format) FROM data WHERE data.book=books.id) formats,
   (SELECT concat(name) FROM data WHERE data.book=books.id) filename,
   (SELECT rating FROM ratings WHERE ratings.id IN (SELECT rating from books_ratings_link WHERE book=books.id)) rating,
    (SELECT concat(name) FROM publishers WHERE publishers.id IN (SELECT publisher from books_publishers_link WHERE book=books.id)) publisher, pubdate, path,
    (SELECT value FROM custom_column_3 WHERE book=books.id) custom_column_3
    FROM books WHERE title like '%{}%'
""".format(queryStr)

cur.execute(querySQL)
queryResult = cur.fetchall()

items = []

for item in queryResult:
    bookID = item[0]
    bookTitle = item[1]
    bookAuthors = item[2].replace("!@#$", ", ")
    bookSize = item[3]
    bookTags = item[4]
    if item[5] is not None:
        bookFormatList = item[5].split("!@#$")
    if item[6] is not None:
        bookFilenameList = item[6].split("!@#$")
#    bookRating = (str(item[7]) + "  ") if isinstance(item[7], int) else "N/A"
    bookPublisher = str(item[8]) if len(str(item[8]))!="" else ""
    bookDate = item[9][0:4]
    bookPath = item[10]
    bookIcon = os.path.join(libraryPath, bookPath, "cover.jpg")

    if item[5] is not None:
        bookFormat = bookFormatList[0]
        bookFilename = bookFilenameList[0]
        temp = {}
        temp["title"] = bookTitle
        temp["icon"] = bookIcon
        temp["subtitle"] = "📙 {:<7} 🏛 {:<5}  ✍️ {}".format(bookFormat, bookPublisher, bookAuthors)
        temp["path"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
        temp["actionArgument"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
        temp['action'] = 'open.sh'
        items.append(temp)
    else:
        temp = {}
        temp["title"] = bookTitle
        temp["icon"] = bookIcon
        temp["subtitle"] = "↗️ DEVONthink 🏛 {:<5}  ✍️ {}".format(bookPublisher, bookAuthors)
        temp["actionArgument"] = re.findall(r"href=\"(.*)\"><span",item[11])[0]
        temp['action'] = 'open.sh'
        items.append(temp)

    # if more than one format
    if len(bookFormatList) > 1:
        for i in range(1, len(bookFormatList)):
            bookFormat = bookFormatList[i]
            bookFilename = bookFilenameList[i]
            temp = {}
            temp["title"] = bookTitle
            temp["icon"] = bookIcon
            temp["subtitle"] = "📙 {:<7} 🏛 {:<5}  ✍️ {}".format(bookFormat, bookPublisher, bookAuthors)
            temp["path"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
            temp["actionArgument"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
            temp['action'] = 'open.sh'
            items.append(temp)

print(json.dumps(items))