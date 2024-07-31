#!/usr/bin/python3
""" Gather data from an API """
import json
import urllib.request


def get_username(users_data, user_id):
    """
    Get the username of a user

    Arguments:
        users_data (list of dictionaries): JSON format of the users' info
        user_id (int): The user ID needed to be fetched

    Return:
        username (str): The username of the user
    """
    for user in users_data:
        if user['id'] == user_id:
            return user['username'].strip()
    return None


def get_user_records(tasks_data, users_data, user_id):
    """
    Get all task records for a specific user

    Arguments:
        tasks_data (list of dictionaries): JSON format of the tasks info
        users_data (list of dictionaries): JSON format of the users' info
        user_id (int): The user ID needed to be fetched

    Return:
        user_tasks (dict): A dictionary of the user's tasks
    """
    user_tasks = []
    user_name = get_username(users_data, user_id)
    for task in tasks_data:
        if task["userId"] == user_id and task["title"] is not None:
            user_tasks.append({"username": user_name,
                               "task": task["title"],
                               "completed": task["completed"]})
    return {str(user_id): user_tasks}


def export_all_tasks_to_json(tasks_data, users_data):
    """
    Export all user task records to a JSON file

    Arguments:
         tasks_data (list of dictionaries): JSON format of the tasks info
         users_data (list of dictionaries): JSON format of the users' info
    """
    all_user_tasks = {}
    for user in users_data:
        user_tasks = get_user_records(tasks_data, users_data, user['id'])
        all_user_tasks.update(user_tasks)

    with open("todo_all_employees.json", 'w', newline='') as json_file:
        json.dump(all_user_tasks, json_file)


if __name__ == '__main__':
    response_tasks = urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/todos')

    if response_tasks.getcode() == 200:
        response_users = urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users')
        if response_users.getcode() == 200:
            tasks_data = json.loads(response_tasks.read().decode('utf-8'))
            users_data = json.loads(response_users.read().decode('utf-8'))
            export_all_tasks_to_json(tasks_data, users_data)
