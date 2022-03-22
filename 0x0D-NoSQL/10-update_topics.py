#!/usr/bin/env python3
""" updates the data inserted
"""


def update_topics(mongo_collection, name, topics):
    """ updates a specifi item in a mongo docuement
    """
    data = mongo_collection.update_one(
        {"name": name}, {"$set": {"topics": topics}}, upsert=True)
    print(data.acknowledged)
