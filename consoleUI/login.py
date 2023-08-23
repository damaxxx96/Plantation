## LOGIN ##
import os
import requests


def login():
    while True:
        print("LOGIN:")
        username = input("Enter username: ")
        password = input("Enter password: ")

        data = {"username": username, "password": password}

        response = requests.post("http://localhost:8000/auth/login/", json=data)

        if response.status_code == 200:
            session = response.cookies.get("sessionid")

            if session:
                return session, username
            else:
                os.system("cls")
                print("Failed retrieving session id")
        else:
            os.system("cls")
            print("Failed login, username or password incorrect")
