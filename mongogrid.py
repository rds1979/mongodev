#!/usr/bin/env python

import gridfs

from pymongo import MongoClient

conn  = MongoClient('127.0.0.1', 27017)
base  = conn.mnemo
coll  = base.files
image = 'img/professor.jpg'

def main():
    grid = gridfs.GridFS(base, 'images')
    imin = open(image, 'rb')
    try:
        _id = grid.put(imin)
        imin.close
        print("идентификатор добавленного файла: ", _id)
        coll.insert({
            'statement' : 'professor',
            'translate' : ['профессор'],
            'categories': ['разговорный', 'научный'],
            'grid_id'   : _id,
            'image'     : image
        })
    except Exception as e:
        print("При добавлении файла произошла ошибка: ", type(e), e)

if __name__ == '__main__':
    main()
