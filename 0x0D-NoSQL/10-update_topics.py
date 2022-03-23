#!/usr/bin/env python3
""" updates the data inserted
"""


def update_topics(mongo_collection, name, topics):
    """ updates a specifi item in a mongo docuement
    """

    mongo_collection.update_many(
        {"name": name}, {'$set': {'topics': topics}})
