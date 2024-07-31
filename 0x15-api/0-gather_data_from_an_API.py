#!/usr/bin/python3
""" Gather data from an API """
import json
import sys
import urllib.request


def get_user_name(user_data, user_id):
    """
    Get the name of a user

    Arguments:
        user_data (list of dictionaries): JSON format of the users' information
        user_id (int): The user id needed to be fetched

    Return:
        name (str): The name of the user
    """

    for user in user_data:
        if user['id'] == user_id:
            return user['name'].strip()

    return None


def get_user_tasks(task_data, user_id):
    """
    Calculate the number of tasks and completed tasks for a specific user

    Arguments:
        task_data (list of dictionaries): JSON format of the tasks information
        user_id (int): The user id needed to be fetched

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

    for task in task_data:
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


if __name__ == '__main__':
    response_tasks = urllib.request.urlopen(
        'https://jsonplaceholder.typicode.com/todos')

    if response_tasks.getcode() == 200:
        response_users = urllib.request.urlopen(
            'https://jsonplaceholder.typicode.com/users')
        if response_users.getcode() == 200:
            task_data = json.loads(response_tasks.read().decode('utf-8'))
            user_data = json.loads(response_users.read().decode('utf-8'))
            if task_data and user_data:
                user_id = int(sys.argv[1])
                total_tasks, completed_tasks_count, completed_task_titles = (
                    get_user_tasks(task_data, user_id))
                user_name = get_user_name(user_data, user_id)

                display_user_tasks_info(total_tasks, completed_tasks_count,
                                        completed_task_titles, user_name)
        else:
            print("Users cannot be retrieved: {}".format(
                response_users.getcode()))
    else:
        print("Tasks cannot be retrieved: {}".format(
            response_tasks.getcode()))
