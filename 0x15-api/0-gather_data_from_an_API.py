#!/usr/bin/python3
"""
fetch information
from jsonplaceholder.typicode.com
"""
import requests
from sys import argv

URL = "https://jsonplaceholder.typicode.com"


def fetch_data(endpoint, *query_params):
    """
    return data from @URL according to endpoint
    and the given qeury
    """
    query = f"{'?' if query_params else ''}{'&'.join(query_params)}"

    data = requests.get(f"{URL}/{endpoint}/{query}").json()

    return data


if __name__ == "__main__":
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit(-1)

    employee_name = fetch_data("users", f"id={employee_id}")[0].get("name")

    employee_all_todos = fetch_data("todos", f"userId={employee_id}")

    employee_completed_todos = fetch_data(
        "todos", f"userId={employee_id}", f"completed=true"
    )

    print(
        f"Employee {employee_name} is done with",
        f"tasks({len(employee_completed_todos)}/{len(employee_all_todos)}):",
    )

    for todo in employee_completed_todos:
        print(f"     {todo.get('title')}")
