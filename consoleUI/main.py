from employee_info import employee_info
from login import login


session, username = login()
name, job = employee_info(session)

print("-----------")
print("WELCOME " + name)
print("--- " + job + " ---")
