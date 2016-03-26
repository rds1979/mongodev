#!/usr/bin/env python

import sys
import datetime

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
base = conn.students
coll = base.grades

def update_one(student_id):
    query = { 'student_id' : student_id, 'type' : 'homework' }
    try:
        row = coll.find_one(query)
        print('before update: ', row)
        row_id = row['_id']
        result = coll.update_one({'_id' : row_id},
                                  { '$set' : { 'review_date' : datetime.datetime.now() } } )
        print('num matched: ', result.matched_count)
        row = coll.find_one({ '_id' : row_id })
        print('after update: ', row)
    except Exception as e:
        raise


def update_many():
    try:
        result = coll.update_many( {}, { '$set' : { 'review_date' : datetime.datetime.now() } } )
        print('num matched: ', result.matched_count)
    except Exception as e:
        raise


def remove_date_many():
    try:
        result = coll.update_many( { 'review_date' : { '$exists' : 'True' } },
                                   { '$unset' : { 'review_date' : 1 } } )
        print('num matched: ', result.matched_count)
    except Exception as e:
        print("При обновлении записи произошла ошибка: ", type(e), e)
        raise


def replace_one(student_id):
    query = { 'student_id' : student_id, 'type' : 'homework' }
    try:
        row = coll.find_one(query)
        print('before update: ', row)
        row['review_date'] = datetime.datetime.now()
        row_id = row['_id']
        coll.replace_one({ '_id' : row_id }, row )
        row = coll.find_one(row_id)
        print('after update: ', row)
    except Exception as e:
        print("При обновлении записи произошла ошибка: ", type(e), e)
        raise

#update_one(2)
#update_many()
#remove_date_many()
replace_one(2)
