#!/usr/bin/env python

import sys
import pymongo

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
base = conn.students
coll = base.grades

def find_lowest_homework():
    query = { 'type' : 'homework' }
    try:
        items = coll.find(query)
        items.sort([('student_id', pymongo.ASCENDING),
                    ('score', pymongo.DESCENDING)])
        counter = 0
        for item in items:
            if (counter %2 == 1):
                row_id = item['_id']
                coll.delete_one({ '_id' : row_id })
                print (row_id)
            counter += 1
    except Exception as e:
        raise

find_lowest_homework()
