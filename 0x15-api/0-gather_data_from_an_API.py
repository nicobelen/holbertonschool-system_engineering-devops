#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""


import requests
import json
import sys


if __name__ == "__main__":

    req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    req_name = req_user.json().get('name')

    req_todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                             .format(sys.argv[1]))
    req_tasks = req_todos.json()

    req_len_tasks = len(req_tasks)
    all_tasks = []
    count = 0

    for task in req_tasks:
        if task["completed"] is True:
            all_tasks.append(task.get('title'))
            count += 1
    print("Employee {} is done with tasks({}/{}):".format(req_name, count, req_len_tasks))

    for title in all_tasks:
        print("\t {}".format(title))
