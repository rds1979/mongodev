#!/usr/bin/env python

import sys
import datetime
import pymongo

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)

def upsert():
    base = conn.students
    coll = base.things
    try:
        coll.drop()
        coll.update_one({ 'thing' : 'apple' }, { '$set' : { 'color' : 'green' } }, upsert = True)
        coll.update_many({ 'thing' : 'banana' }, { '$set' : { 'color' : 'yellow' } }, upsert = True)
        coll.update_one({ 'thing' : 'apple' }, { '$set' : { 'color' : 'red' } }, upsert = True)
    except Exception as e:
        print("При изменении записи произошла ошибка: ", type(e), e)
        raise


def get_next(name):
    base = conn.students
    coll = base.counter
    try:
        counter = coll.find_one_and_update( filter = { 'type' : name },
                                            update = { '$inc' : { 'value' : -1 } },
                                            upsert = True,
                                            return_document = pymongo.ReturnDocument.AFTER )
    except Exception as e:
        print("При изменении записи произошла ошибка: ", type(e), e)
        raise
    counter_value = counter['value']
    return counter_value


def remove(student_id):
    base = conn.students
    coll = base.grades
    try:
        result = coll.delete_many({ 'student_id' : student_id })
        print("num removed: ", result.deleted_count)
    except Exception as e:
        print("При удалении записи произошла ошибка: ", type(e), e)
        raise


#print(get_next('uid'))
#print(get_next('uid'))
#print(get_next('uid'))

#upsert()

remove(1)
