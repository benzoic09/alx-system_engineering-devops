#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    username = user.json().get("username")

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

    # Create a CSV file with user ID as the filename
    filename = "{}.csv".format(userId)

    # Write data to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todos.json():
            if task.get('userId') == int(userId):
                task_status = "True" if task.get('completed') else "False"
                csvwriter.writerow(
                    [userId, username, task_status, task.get('title')])
