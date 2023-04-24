#!/usr/bin/python3
"""Script to gather data from an API"""
import json
import re
import requests
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if (len(argv) > 1):
        id = int(argv[1])
        todos_result = requests.get('{}/todos'.format(API_URL)).json()
        users_result = requests.get('{}/users/{}'.format(API_URL, id)).json()
        username = users_result.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_result))
        todos_list = []
        for todo in todos:
            todo_dict = {}
            todo_dict.update({"task": todo.get("title"), "completed": todo.get(
                             "completed"), "username": username})
            todos_list.append(todo_dict)
        with open("{}.json".format(argv[1]), 'w') as f:
            json.dump({argv[1]: todos_list}, f)
