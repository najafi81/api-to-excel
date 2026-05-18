import requests
from openpyxl import Workbook

API_URL="https://jsonplaceholder.typicode.com/users"

response=requests.get(API_URL)
response.raise_for_status()

users=response.json()

workbook=Workbook()
sheet=workbook.active
sheet.title="Users"

sheet.append(["ID","Name","Username","Email","City","Company"])

for user in users:
    sheet.append([
            user["id"],
            user["name"],
            user["username"],
            user["email"],
        #    user["city"],
            user["address"]["city"],
            user["company"]["name"]
    ])

workbook.save("users.xlsx")

print("Excel file created successfully.")
