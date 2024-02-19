#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list
progress and exports data in CSV format.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user information
    user_response = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch user's tasks
    todos_response = requests.get(
            "https://jsonplaceholder.typicode.com/todos", params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Tasks not found for the user.")
        sys.exit(1)

    todos = todos_response.json()

    # Prepare CSV data
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in todos:
        task_completed_status = "Yes" if task.get('completed') else "No"
        csv_data.append([user_id, username, task_completed_status, task.get('title')])

    # Write CSV data to file
    csv_filename = "{}.csv".format(user_id)
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_data)

    print("CSV file '{}' has been generated.".format(csv_filename))

