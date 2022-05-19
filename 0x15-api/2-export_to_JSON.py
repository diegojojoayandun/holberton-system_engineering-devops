#!/usr/bin/python3
""" extend your Python script to export data in the JSON format """

import json
import requests
from sys import argv

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(url + "/users/{}".
                        format(argv[1]), verify=False).json()
    todo = requests.get(url + "/todos?userId={}".
                        format(argv[1]), verify=False).json()
    username = user.get('username')
    tasks = []

    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)

    jsonobj = {}

    jsonobj[argv[1]] = tasks

    with open("{}.json".format(argv[1]), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
