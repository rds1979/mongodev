#!/usr/bin/env python

import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
base = conn.school
coll = base.students

try:
    cursor = coll.find({}, {'scores' : 1})
    for entry in cursor:
        student_id = entry['_id']
        scores     = entry['scores']

        my_list = []

        for score in scores:
            if score['type'] == 'homework':
                my_list.append(score['score'])
        my_list.sort()
        scores.remove({'type' : 'homework', 'score' : my_list[0]})
        coll.update({ '_id' : student_id }, { '$set' : { 'scores' : scores} })
except Exception as e:
    print("Произошла ошибка: ", type(e), e)
    raise
