#!/usr/bin/env python3
"""Lists all documents in python"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection

    :Return [] if no doc in the collection
    """
    return mongo_collection.find()
