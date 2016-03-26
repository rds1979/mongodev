#!/usr/bin/env python

import bottle
from pymongo import MongoClient
from json import dumps

@bottle.route('/')
def index():
    conn = MongoClient('localhost', 27017)
    base = conn.dictionaries
    coll = base.enru

    try:
        words = coll.find()
        for word in words:
            return word['statement']

    except Exception as e:
        print("При поиске записи произошла ошибка: ", type(e), e)

bottle.debug(True)
bottle.run(host='localhost', port=8081)
