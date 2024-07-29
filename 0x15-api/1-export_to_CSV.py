#!/usr/bin/python3
"""
This script returns an argument and displays employee 
information
"""
import requests
import sys
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    
    # Fetch user details
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("name")
    
    # Fetch tasks for the user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    
    # Prepare data for CSV
    tasks_data = [
        [user_id, username, 'Completed' if t.get("completed") else 'Not Completed', t.get("title")]
        for t in todos
    ]
    
    # Create CSV filename
    csv_filename = f"{user_id}.csv"
    
    # Write to CSV file
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        # Write data rows
        writer.writerows(tasks_data)
    
    print(f"Tasks have been saved to {csv_filename}")
