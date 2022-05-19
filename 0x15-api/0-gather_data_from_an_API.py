#!/usr/bin/python3
""" Return information about the employee's todo list progress """

import requests
from sys import argv

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(url + "/users/{}".
                        format(argv[1]), verify=False).json()
    todo = requests.get(url + "/todos?userId={}".
                        format(argv[1]), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
