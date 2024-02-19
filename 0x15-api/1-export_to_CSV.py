#!/usr/bin/python3
"""Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list
progress and exports data in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user information
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch user's tasks
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Prepare CSV data
    csv_data = [
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]
    for task in todos:
        task_completed_status = "Yes" if task.get('completed') else "No"
        csv_data.append(
                [user_id, username, task_completed_status, task.get('title')])

    # Write CSV data to file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_data)
