#!/usr/bin/env python

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
base = conn.dictionaries
coll = base.enru

word = {
    'statement' : 'improve',
    'translate' : ['улучшать', 'совершенствовать', 'выправлять'],
    'categories': ['технический']
}

try:
    words = base.enru
    word_id = words.insert_one(word).inserted_id
    print(word_id, word['statement'])

except Exception as e:
    print("При добавлении записи произошла ошибка: ", type(e), e)
