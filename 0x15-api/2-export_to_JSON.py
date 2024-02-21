#!/usr/bin/python3
"""
Python script that, using a REST API,
exports data in JSON format for all employees' tasks.
"""

import json
import requests
import sys

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    # Organize tasks by user ID
    tasks_by_user = {}
    for task in todos.json():
        userId = sys.argv[1]
        if userId not in tasks_by_user:
            tasks_by_user[userId] = []
        tasks_by_user[userId].append({
            'username': [user['username'] for user in users.json()
                         if user['id'] == userId],
            'task': task.get('title'),
            'completed': task.get('completed')
        })

    # Write data to JSON file
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(tasks_by_user, jsonfile, indent=4)
