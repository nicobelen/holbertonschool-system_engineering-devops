#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""


import json
import requests
import sys


if __name__ == "__main__":

    req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    req_name = req_user.json().get('username')

    req_todos = requests.get('https://jsonplaceholder.typicode.com/users/\
{}/todos'.format(sys.argv[1]))
    req_tasks = req_todos.json()

    list_user = []
    dict_user = {sys.argv[1]: list_user}

    for task in req_tasks:
        list_user.append({"task": task.get('title'),
                          "completed": task.get('completed'),
                          "username": req_name})

    with open(sys.argv[1] + '.json', 'w', encoding='utf-8') as f:
        json.dump(dict_user, f)
