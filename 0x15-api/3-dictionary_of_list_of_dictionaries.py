#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress."""


import json
import requests


if __name__ == "__main__":

    req_users = requests.get('https://jsonplaceholder.typicode.com/users')
    req_users = req_users.json()

    def user_list(id):

        req_user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                                .format(id))
        req_name = req_user.json().get('username')

        req_todos = requests.get('https://jsonplaceholder.typicode.com/users/\
{}/todos'.format(id))
        req_tasks = req_todos.json()

        list_user = []

        for task in req_tasks:
            list_user.append({"username": req_name,
                              "task": task.get('title'),
                              "completed": task.get('completed')})
        return list_user

    dict_users = {}
    for user in req_users:
        dict_users.update({user.get('id'): user_list(user.get('id'))})
    with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
        json.dump(dict_users, f)
