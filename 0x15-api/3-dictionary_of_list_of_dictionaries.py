#!/usr/bin/python3
"""Script to gather data from an API"""
import json
import re
import requests
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    todos_result = requests.get('{}/todos'.format(API_URL)).json()
    users_result = requests.get('{}/users'.format(API_URL)).json()
    users_dict = {}
    for user in users_result:
        id = user.get('id')
        username = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_result))
        user_dict = list(map(
            lambda x: {
                'username': username,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_dict[id] = user_dict
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
