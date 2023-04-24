#!/usr/bin/python3
"""Script to gather data from an API"""
import re
import requests
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    if (len(argv) > 1):
        id = int(argv[1])
        todos_result = requests.get('{}/todos'.format(API_URL)).json()
        users_result = requests.get('{}/users/{}'.format(API_URL, id)).json()
        name = users_result.get('name')
        todos = list(filter(lambda x: x.get('userId') == id, todos_result))
        completed = list(filter(lambda x: x.get('completed'), todos))
        print("Employee {} is done with tasks({}/{}):"
              .format(name, len(completed), len(todos)))
        for todo in completed:
            print('\t {}'.format(todo.get('title')))
