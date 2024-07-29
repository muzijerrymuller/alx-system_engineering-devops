#!/usr/bin/python3
"""
Takes an argument and displays
employee information
in csv format
"""

import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("name")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks_data = [
        [user_id, username, 'Completed' if t.get("completed") else 'Not Completed', t.get("title")]
        for t in todos
    ]

    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        writer.writerows(tasks_data)

    print(f"Tasks have been saved to {csv_filename}")
