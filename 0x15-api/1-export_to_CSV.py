#!/usr/bin/python3
""" To Cvs """

import csv
import requests
from sys import argv

if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(url + "/users/{}".
                        format(argv[1]), verify=False).json()
    todo = requests.get(url + "/todos?userId={}".
                        format(argv[1]), verify=False).json()
    with open("{}.csv".format(argv[1]), 'w', newline='') as csvfile:
        todo_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for _item in todo:
            todo_writer.writerow([int(argv[1]), user.get('username'),
                                 _item.get('completed'),
                                 _item.get('title')])
