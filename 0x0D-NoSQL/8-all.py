#!/usr/bin/env python3
""" craeates a connection with mongo
"""


def list_all(mongo_collection):
    """return all the collections obtained
    """
    documents = mongo_collection.find()
    if documents.retrieved == 0:
        return []
    return documents
