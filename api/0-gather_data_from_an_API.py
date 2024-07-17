#!/usr/bin/python3
"""
    Interacts with a REST API to get information about
    employees
"""


import json
import sys
import urllib.request

base = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    url = base + "users/{}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        user_data = response.read()
    user = json.loads(user_data)
    employee_name = user["name"]

    url = base + "todos?userId={}".format(employee_id)
    with urllib.request.urlopen(url) as response:
        todos_data = response.read()
    todos = json.loads(todos_data)

    completed = [todo["title"] for todo in todos if todo["completed"]]
    total = len(todos)
    completed_tasks_len = len(completed)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks_len, total))

    for task in completed:
        print("\t {}".format(task))
