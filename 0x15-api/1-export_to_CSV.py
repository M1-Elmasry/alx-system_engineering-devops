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
        empl_id = int(argv[1])
    except ValueError:
        exit(-1)

    employee_usrname = fetch_data("users", f"id={empl_id}")[0].get("username")

    employee_all_todos = fetch_data("todos", f"userId={empl_id}")

    filename = f"{empl_id}.csv"

    with open(filename, mode="w", newline="\n") as file:

        for todo in employee_all_todos:
            line = ",".join(
                [
                    f"\"{empl_id}\"",
                    f"\"{employee_usrname}\"",
                    f"\"{todo.get('completed')}\"",
                    f"\"{todo.get('title')}\"",
                ]
            )

            line += "\n"

            file.write(line)
