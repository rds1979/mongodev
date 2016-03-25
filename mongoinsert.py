#!/usr/bin/env python

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
base = conn.dictionaries
coll = base.enru

def insert(word):
    try:
        word_id = coll.insert_one(word).inserted_id
        print(word_id, word['statement'])
    except Exception as e:
        print("При добавлении записи произошла ошибка: ", type(e), e)

improve = {
    'statement' : 'improve',
    'translate' : ['улучшать', 'совершенствовать', 'выправлять'],
    'categories': ['технический']
}

# insert(improve)

def insert_many():
    connect = {
        'statement' : 'connect',
        'translate' : ['соединять', 'связывать'],
        'categories': ['технический']
    }
    executable = {
        'statement' : 'executable',
        'translate' : ['исполняемый'],
        'categories': ['технический']
    }
    words_to_insert = [connect, executable]
    try:
        coll.insert_many(words_to_insert, ordered = False)
    except Exception as e:
        print("При добавлении записи произошла ошибка: ", type(e), e)

insert_many()
