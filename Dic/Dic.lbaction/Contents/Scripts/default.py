#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-
#
# LaunchBar Action Script
#
import sys
import json
import re
import ctypes
from ctypes.util import find_library

class CFRange(ctypes.Structure):
    _fields_ = [
        ("location", ctypes.c_long),
        ("length", ctypes.c_long),
    ]


CoreServices = ctypes.cdll.LoadLibrary(find_library("CoreServices"))
CoreFoundation = ctypes.cdll.LoadLibrary(find_library("CoreFoundation"))

kCFStringEncodingUTF8 = 0x08000100

CoreFoundation.CFStringCreateWithCString.restype = ctypes.c_void_p
CoreFoundation.CFStringCreateWithCString.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_uint32,
]

CoreFoundation.CFStringGetCString.restype = ctypes.c_bool
CoreFoundation.CFStringGetCString.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_long,
    ctypes.c_uint32,
]

CoreFoundation.CFRelease.argtypes = [ctypes.c_void_p]

CoreServices.DCSCopyTextDefinition.restype = ctypes.c_void_p
CoreServices.DCSCopyTextDefinition.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    CFRange,
]


def cfstring_to_py(cfstr):
    if not cfstr:
        return None

    buf = ctypes.create_string_buffer(1024 * 1024)
    ok = CoreFoundation.CFStringGetCString(
        cfstr,
        buf,
        len(buf),
        kCFStringEncodingUTF8,
    )
    if not ok:
        return None

    return buf.value.decode("utf-8")


def lookup(word: str):
    cf_word = CoreFoundation.CFStringCreateWithCString(
        None,
        word.encode("utf-8"),
        kCFStringEncodingUTF8,
    )

    if not cf_word:
        return None

    try:
        result = CoreServices.DCSCopyTextDefinition(
            None,
            cf_word,
            CFRange(0, len(word)),
        )

        try:
            return cfstring_to_py(result)
        finally:
            if result:
                CoreFoundation.CFRelease(result)

    finally:
        CoreFoundation.CFRelease(cf_word)

items = []

text = lookup(sys.argv[1])
text = text.replace('e.g.', 'e<DOT>g<DOT>')

parts = re.split(r'[.|]', text)
for part in parts[1:]:
    part = part.replace('e<DOT>g<DOT>', 'e.g.').strip()
    if not part.strip():
        continue

    item = {}
    item['title'] = part
    item['action'] = "openlink.py"
    item['actionArgument'] = sys.argv[1]
    item['actionRunsInBackground'] = True
    items.append(item)

print(json.dumps(items))