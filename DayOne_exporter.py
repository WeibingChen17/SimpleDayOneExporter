#!/usr/bin/python3
import os
import time
import sqlite3
from datetime import datetime
from datetime import timedelta

DAYONE_DATABASE = "./DayOne.sqlite"

# Offset due to MacOs Core Data library:
offset_year = (datetime(2001, 1, 1) - datetime(1970, 1, 1)).total_seconds()

def getCreateDateTimestamp(row):
    ts = row[18]
    return int(getRightTimestamp(ts))

def getModifyDateTimestamp(row):
    ts = row[19]
    return int(getRightTimestamp(ts))

def getRightTimestamp(ts):
    return ts + offset_year - time.timezone

def getTitle(row):
    ti = getMarkdownText(row).split('\n')
    if not ti:
        return 'Empty content ' + str(random.rand(100000))
    ti = ti[0]
    return ti.replace('\\', '').replace('#', '').replace('/', '-').strip()

def getMarkdownText(row):
    return row[28]

conn = sqlite3.connect(DAYONE_DATABASE)
cursor = conn.execute("SELECT * FROM ZENTRY")

row = cursor.fetchone()
ct = getCreateDateTimestamp(row)
mt = getModifyDateTimestamp(row)
title = getTitle(row)
text = getMarkdownText(row)
if title:
    filename = title + '.md'
    print('generating ' + filename)
    with open(filename, 'w') as f:
        f.write(text)
    os.utime(filename, (ct, mt))
