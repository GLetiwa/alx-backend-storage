#!/usr/bin/env python3
"""python function"""


def schools_by_topic(mongo_collection, topic):
    """changes all topics of a school document based on the name"""
    return mongo_collection.find({"topics": topic})
