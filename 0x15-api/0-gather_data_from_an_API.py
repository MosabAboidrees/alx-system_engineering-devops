#!/usr/bin/python3
""" Gather data from an API """

import requests
import sys


def to_do_list(emp_id):
    """ Fetches employee TODO list """

    url = "https://jsonplaceholder.typicode.com/users"
    user_response = requests.get(f"{url}/{emp_id}")

    if user_response.status_code != 200:
        print(f"Error: Employee ID {emp_id} not found.")
        return

    user_data = user_response.json()
    name = user_data.get("name")

    if name:
        todos_response = requests.get(f"{url}/{emp_id}/todos")
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task.get/
                ("completed")]
        num_completed_tasks = len(completed_tasks)

        print(f"Employee {name} is done with tasks/
                ({num_completed_tasks}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        EMPLOYEE_ID = int(sys.argv[1])
        to_do_list(EMPLOYEE_ID)
    except ValueError:
        print("The employee ID must be an integer.")
