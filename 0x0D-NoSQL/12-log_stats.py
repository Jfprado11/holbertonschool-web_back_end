#!/usr/bin/env python3
"""passing a value to find in the logs ngix
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    ngix_logs_collections = client.logs.nginx

    all_documents = ngix_logs_collections.count_documents({})
    print("{} logs".format(all_documents))
    print("Methods:")
    get_log = ngix_logs_collections.find({"method": "GET"})
    post_log = ngix_logs_collections.find({"method": "POST"})
    put_log = ngix_logs_collections.find({"method": "PUT"})
    patch_log = ngix_logs_collections.find({"method": "PATCH"})
    delete_log = ngix_logs_collections.find({"method": "DELETE"})
    status = ngix_logs_collections.find({"method": "GET", "path": "/status"})

    print("\tmethod GET: {}".format(len(list(get_log))))
    print("\tmethod POST: {}".format(len(list(post_log))))
    print("\tmethod PUT: {}".format(len(list(put_log))))
    print("\tmethod PATCH: {}".format(len(list(patch_log))))
    print("\tmethod DELETE: {}".format(len(list(delete_log))))
    print("{} status check".format(len(list(status))))
