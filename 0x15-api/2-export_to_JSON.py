#!/usr/bin/python3

""" Gather data from an API """
import csv
import json
import sys
import urllib.request


def get_user_name(users_data, user_id):
    """
    Get the name of a user

    Arguments:
        users_data (list of dictionaries): JSON format of the users' info
        user_id (int): The user ID needed to be fetched

    Return:
        name (str): The name of the user
    """
    for user in users_data:
        if user['id'] == user_id:
            return user['name'].strip()
    return None


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


def get_user_tasks_info(tasks_data, user_id):
    """
    Calculate the number of tasks and completed tasks for a specific user

    Arguments:
        tasks_data (list of dictionaries): JSON format of the tasks info
        user_id (int): The user ID needed to be fetched

    Return:
        total_tasks (int): The total number of tasks
        completed_tasks_count (int): The number of completed tasks
        completed_task_titles (list): The list of completed task titles
    """
    total_tasks = 0
    completed_tasks_count = 0
    completed_task_titles = []

    if not isinstance(user_id, int):
        raise TypeError('user_id must be an integer')

    for task in tasks_data:
        if task['userId'] == user_id and task['title'] is not None:
            total_tasks += 1
            if task['completed']:
                completed_tasks_count += 1
                completed_task_titles.append(task['title'])

    return total_tasks, completed_tasks_count, completed_task_titles


def display_user_tasks_info(total_tasks, completed_tasks_count,
                            completed_task_titles, user_name):
    """
    Print information about the user's tasks

    Arguments:
        total_tasks (int): The total number of tasks
        completed_tasks_count (int): The number of completed tasks
        completed_task_titles (list): The list of completed task titles
        user_name (str): The name of the user
    """
    if not isinstance(total_tasks, int):
        raise TypeError('total_tasks must be an integer')
    if not isinstance(completed_tasks_count, int):
        raise TypeError('completed_tasks_count must be an integer')
    if not isinstance(completed_task_titles, list):
        raise TypeError('completed_task_titles must be a list')

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, completed_tasks_count, total_tasks))
    for task_title in completed_task_titles:
        print("\t {}".format(task_title))


def save_tasks_to_csv(tasks_data, users_data, user_id):
    """
    Save tasks data to a CSV file

    Arguments:
        tasks_data (list of dictionaries): JSON format of the tasks info
        users_data (list of dictionaries): JSON format of the users' info
        user_id (int): The user ID needed to be fetched
    """
    user_records = []
    user_name = get_username(users_data, user_id)
    for task in tasks_data:
        if task['userId'] == user_id and task['title'] is not None:
            record = [user_id, user_name, task['completed'], task['title']]
            user_records.append(record)

    with open(f'{user_id}.csv', mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in user_reco
        csv_writer.writerow(row)


def save_tasks_to_json(tasks_data, users_data, user_id):
    """
    Save tasks data to a JSON file

    Arguments:
        tasks_data (list of dictionaries): JSON format of the tasks info
        users_data (list of dictionaries): JSON format of the users' info
        user_id (int): The user ID needed to be fetched
    """
    all_records = []
    user_name = get_username(users_data, user_id)
    for task in tasks_data:
        if task["userId"] == user_id and task["title"] is not None:
            all_records.append({"task": task["title"],
                                "completed": task["completed"],
                                "username": user_name})
    user_tasks = {str(user_id): all_records}

    with open(f"{user_id}.json", 'w', newline='') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == '__main__':
    response_tasks = urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/todos')

    if response_tasks.getcode() == 200:
        response_users = urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users')
        if response_users.getcode() == 200:
            tasks_data = json.loads(response_tasks.read().decode('utf-8'))
            users_data = json.loads(response_users.read().decode('utf-8'))
            save_tasks_to_json(tasks_data, users_data, int(sys.argv[1]))
