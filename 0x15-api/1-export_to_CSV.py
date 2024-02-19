#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]

    # Fetch user information
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    user_data = user.json()
    username = user_data.get('username')

    # Fetch user's tasks
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    user_tasks = [task for task in todos.json() if task.get('userId') == int(userId)]

    # Prepare CSV data
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in user_tasks:
        task_completed_status = "Yes" if task.get('completed') else "No"
        csv_data.append([userId, username, task_completed_status, task.get('title')])

    # Write CSV data to file
    filename = f"{userId}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_data)

    print(f"CSV file '{filename}' has been generated.")
