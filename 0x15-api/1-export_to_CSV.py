#!/usr/bin/python3
"""
fetch information
from jsonplaceholder.typicode.com
"""
import requests
from sys import argv
from csv import writer as csv_writer

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

    employee_username = fetch_data("users", f"id={employee_id}")[0].get("username")

    employee_all_todos = fetch_data("todos", f"userId={employee_id}")

    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="") as file:
        writer = csv_writer(file)
        for todo in employee_all_todos:
            writer.writerow(
                [
                    employee_id,
                    employee_username,
                    f"{todo.get('completed')}",
                    f"{todo.get('title')}",
                ]
            )
