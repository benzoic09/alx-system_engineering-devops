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

    # Filter tasks for the specified user ID
    user_tasks = [{"task": task.get("title"), "completed":
                   task.get("completed"), "username": username}
                  for task in todos if task.get("userId") == int(userid)]

    # Write data to JSON file
    with open("{}.json".format(userid), 'w') as jsonfile:
        json.dump(user_tasks, jsonfile, indent=4)
