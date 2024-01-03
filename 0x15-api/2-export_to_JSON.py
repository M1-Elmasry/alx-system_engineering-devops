#!/usr/bin/python3
"""
fetch information
from jsonplaceholder.typicode.com
"""
import requests
from sys import argv
import json

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
        empl_id = int(argv[1])
    except ValueError:
        exit(-1)

    employee_usrname = fetch_data("users", f"id={empl_id}")[0].get("username")

    employee_all_todos = fetch_data("todos", f"userId={empl_id}")

    json_object = {empl_id: []}

    for todo in employee_all_todos:
        json_object.get(empl_id).append(
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_usrname,
            }
        )

    filename = f"{empl_id}.json"

    with open(filename, mode="w") as file:
        json.dump(json_object, file)
