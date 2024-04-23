#!/usr/bin/python3
"""extend Python script to export data in the JSON format"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    t_user = {}
    t_list = []

    for task in todos:
        if task.get('userId') == int(userId):
            t_dict = {"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": user.json().get('username')}
            t_list.append(t_dict)
    t_user[userId] = t_list
    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(t_user, f)
