#!/usr/bin/python3
"""
Python script that, using a REST API,
exports data in JSON format for all employees' tasks.
"""

import json
import requests

if __name__ == "__main__":
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    # Create a dictionary to store data for all employees
    all_data = {}

    for user in users:
        user_id = str(user['id'])
        username = user['username']

        user_tasks = []
        for task in todos:
            if task['userId'] == user['id']:
                user_tasks.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        all_data[user_id] = user_tasks

    # Write data to JSON file
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(all_data, jsonfile, indent=4)
