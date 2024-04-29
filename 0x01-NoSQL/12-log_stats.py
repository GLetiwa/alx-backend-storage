#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB:
- Database: logs
- Collection: nginx
"""


import pymongo


def log_stats():
    """Prints some stats about Nginx logs stored in MongoDB"""

    # Connect to MongoDB
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Number of logs with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
