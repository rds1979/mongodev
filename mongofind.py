#!/usr/bin/env python
import sys

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
base = conn.students
coll = base.grades

def find_with_glt():
    query = { '$and' : [ { 'type' : 'exam' },{ 'score' : { '$gte' : 65, '$lte' : 80 } } ] }
    try:
        items = coll.find(query).skip(10).limit(10)
    except Exception as e:
        print("При поиске записи произошла ошибка: ", type(e), e)

    for item in items:
        print(item['type'], ':', item['score'])

def find_one(student_id):
    query = { 'student_id' : student_id }
    try:
        item = coll.find_one(query)
    except Exception as e:
        print("При поиске записи произошла ошибка: ", type(e), e)

    print(item['type'], ':', item['score'])

def find_with_regex():
    query = { 'type' : { '$regex' : 'exam|quiz', '$options' : 'i' } }
    projn = { 'student_id' : 1, 'type' : 1, 'score' : 1 }
    try:
        items = coll.find(query, projn).limit(10)
    except Exception as e:
        print("При поиске записи произошла ошибка: ", type(e), e)

    for item in items:
        for key in sorted(item):
            print(key, ':', item[key])

find_with_regex()
