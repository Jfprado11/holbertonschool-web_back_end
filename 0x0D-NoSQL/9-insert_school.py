#!/usr/bin/env python3
""" iserting in a document
"""


from multiprocessing.sharedctypes import Value


def insert_school(mongo_collection, **kwargs):
    """ iserting into a mongo db for kwargs
    """
    data_to_insert = {}
    for arg, value in kwargs.items():
        data_to_insert[arg] = value
    data = mongo_collection.insert_one(data_to_insert)
    return data.inserted_id
