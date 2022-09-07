#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""


import csv
import requests
import sys


if __name__ == "__main__":

    req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    req_name = req_user.json().get('username')

    req_todos = requests.get('https://jsonplaceholder.typicode.com/users/\
{}/todos'.format(sys.argv[1]))
    req_tasks = req_todos.json()

    with open(sys.argv[1] + '.csv', 'w') as f:
        my_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in req_tasks:
            my_writer.writerow([sys.argv[1], req_name, task.get('completed'),
                                task.get('title')])
