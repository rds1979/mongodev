#!/usr/bin/env python

import gridfs

from pymongo import MongoClient

conn  = MongoClient('127.0.0.1', 27017)
base  = conn.mnemo
coll  = base.files
image = 'img/university.jpg'

def main():
    grid = gridfs.GridFS(base, 'images')
    imin = open(image)

    _id = grid.put(imin)
    imin.close
    print("идентификатор добавленного файла: ", _id)

    coll.insert({
        'statement' : 'university',
        'translate' : ['университет'],
        'categories': ['разговорный', 'научный'],
        'grid_id'   : _id,
        'image'     : image
    })

if __name__ == '__main__':
    main()
