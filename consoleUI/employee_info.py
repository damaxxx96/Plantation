import requests
import json


def employee_info(session_id):
    response = requests.get(
        "http://localhost:8000/employee/info/self",
        headers={"Cookie": "sessionid=" + session_id},
    )
    data = json.loads(response.text)

    return data["name"], data["job"]
