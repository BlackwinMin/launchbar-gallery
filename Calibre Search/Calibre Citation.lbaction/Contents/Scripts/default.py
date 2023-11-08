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
queryStr = queryStr.replace(" ", "%")
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
    (SELECT value FROM custom_column_3 WHERE book=books.id) custom_column_3,
    (SELECT value FROM custom_column_4 WHERE book=books.id) custom_column_4
    FROM books
    WHERE (books.title like '%{}%') OR (books.author_sort like '%{}%')
""".format(queryStr, queryStr)

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
    else:
        bookFormatList = "N"
    if item[6] is not None:
        bookFilenameList = item[6].split("!@#$")
    else:
        bookFilenameList = "N"
#    bookRating = (str(item[7]) + "  ") if isinstance(item[7], int) else "N/A"
    bookPublisher = str(item[8]) if len(str(item[8]))!="" else ""
    bookDate = item[9][0:4]
    bookPath = item[10]
    bookIcon = os.path.join(libraryPath, bookPath, "cover.jpg")
    if item[12] is not None:
        FirstPublished = item[12][0:4]
    else:
        FirstPublished = "Null"

    temp = {}
    temp["title"] = bookTitle
    temp["icon"] = bookIcon
    temp['action'] = 'citation.sh'
    if bookAuthors.startswith(("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")):
        temp["actionArgument"] = bookAuthors + ", *" + bookTitle + "* (" + bookPublisher + ", " + bookDate + ")."
    else:
        temp["actionArgument"] = bookAuthors + "：《" + bookTitle + "》，" + bookPublisher + bookDate + "年版。"

    if item[5] is not None:
        bookFormat = bookFormatList[0]
        bookFilename = bookFilenameList[0]
        temp["subtitle"] = "ID{} 📙 {:<7} 🗓 {} FirstPub {} 🏛 {:<5} ✍️ {}".format(bookID, bookFormat, bookDate, FirstPublished, bookPublisher, bookAuthors)
        temp["path"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
        temp["quickLookURL"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
        items.append(temp)
    else:
        temp["subtitle"] = "ID{} ↗️ External 🗓 {} FirstPub {} 🏛 {:<5} ✍️ {}".format(bookID, bookDate, FirstPublished, bookPublisher, bookAuthors)
        if re.findall(r"href=\"file:\/\/([^\"]*)\">",item[11]):
            temp["path"] = re.findall(r"href=\"file:\/\/([^\"]*)\">",item[11])[0]
        else:
            temp["path"] = re.findall(r"href=\"([^\"]*)\">",item[11])[0]
        items.append(temp)

    # if more than one format
    if len(bookFormatList) > 1:
        for i in range(1, len(bookFormatList)):
            bookFormat = bookFormatList[i]
            bookFilename = bookFilenameList[i]
            temp["subtitle"] = "ID{} 📙 {:<7} 🗓 {} FirstPub {} 🏛 {:<5} ✍️ {}".format(bookID, bookFormat, bookDate, FirstPublished, bookPublisher, bookAuthors)
            temp["path"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
            temp["quickLookURL"] = os.path.join(libraryPath, bookPath, bookFilename + "." + bookFormat.lower())
            items.append(temp)

print(json.dumps(items))