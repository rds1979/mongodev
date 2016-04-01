#!/usr/bin/env python

import sys
import datetime

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
base = conn.students
coll = base.persones

def insert_row(row):
    try:
        coll.update_one(row, { '$set' : { 'date_add' : datetime.datetime.now() } }, upsert = True)
    except Exception as e:
        print("При добавлении, изменении записи произошла ошибка: ", type(e), e)
        raise


file = open('txt/npersone.txt')
text = file.read()
line = text.rstrip()

(lname, fname, mname) = line.split()
row = {
    'name' : {
         'lname' : lname,
         'fname' : fname,
         'mname' : mname
    },
    'fields' : ['python', 'mongodb', 'pymongo']
}

row['gender'] = 1
fields = row['fields']
fields.append('django')

insert_row(row)
