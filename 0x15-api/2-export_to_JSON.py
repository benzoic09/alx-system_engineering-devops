#!/usr/bin/python3
"""
Python script that, using a REST API,
exports data in JSON format for all employees' tasks.
"""

import json
import requests
import sys

if __name__ == "__main__":
    userid = sys.argv[1]

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(userid)).json()
    username = users.get("username")

    # Write data to JSON file
    with open("{}.json".format(userid), "w") as jsonfile:
        json.dump({userid: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
