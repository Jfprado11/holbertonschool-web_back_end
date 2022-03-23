#!/usr/bin/env python3
"""passing to return a specifi topic in mongo
"""


def schools_by_topic(mongo_collection, topic):
    """returns a specif topics
    """
    data = mongo_collection.find({"topics": {"$in": [topic]}})
    return data
