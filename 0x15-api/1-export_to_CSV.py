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
        username = users_result.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_result))
        with open("{}.csv".format(id), 'w') as f:
            for todo in todos:
                f.write(
                        '"{}","{}","{}","{}"\n'.format(
                            id,
                            username,
                            todo.get('completed'),
                            todo.get('title')
                        )
                )
