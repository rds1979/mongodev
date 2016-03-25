#!/usr/bin/env python

"""
Write a program in the language of your choice
that will remove the grade of type "homework"
with the lowest score for each student from the
dataset in the handout.
"""

from pymongo import MongoClient

conn = MongoClient('localhost', 27017)
base = conn.students
coll = base.grades
