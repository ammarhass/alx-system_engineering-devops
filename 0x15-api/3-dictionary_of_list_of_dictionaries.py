#!/usr/bin/python3
"""extend Python script to export data in the JSON format"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    t_all = {}

    for user in users:
        t_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                t_dict = {"username": user.get('username'),
                          "task": task.get('title'),
                          "completed": task.get('completed')}
                t_list.append(t_dict)
        t_all[user.get('id')] = t_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(t_all, f)
