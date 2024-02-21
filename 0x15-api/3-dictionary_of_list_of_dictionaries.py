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

    # Write data to JSON file
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump({
            u.get("id"): [{"task": t.get("title"),
                          "completed": t.get("completed"), "username": u.get("username")
                           } for t in requests.get(todos,
                                                   params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
