#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress and exports data in JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user information
    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch user's tasks
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": user_id})
    if todos_response.status_code != 200:
        print("Tasks not found for the user.")
        sys.exit(1)

    todos = todos_response.json()

    # Prepare JSON data
    json_data = {"USER_ID": []}
    for task in todos:
        task_completed_status = "Yes" if task.get('completed') else "No"
        json_data["USER_ID"].append({"task": task.get('title'), "completed": task_completed_status, "username": username})

    # Write JSON data to file
    json_filename = "{}.json".format(user_id)
    with open(json_filename, "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print("JSON file '{}' has been generated.".format(json_filename))
