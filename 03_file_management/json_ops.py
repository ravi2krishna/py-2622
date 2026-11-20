# Working With JSON Files / Data

import json 

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))

print(student)

# Write Student Data To JSON File
with open("03_file_management/student.json","w") as file_data:
    json.dump(student,file_data)

# Write Student Data To JSON File, With JSON formatting
with open("03_file_management/student.json","w") as file_data:
    json.dump(student,file_data,indent=4)
    
# Read Student Data From JSON File
with open("03_file_management/student.json","r") as file_data:
    data = json.load(file_data)
    print("Data From JSON File: ",data)
    print(type(data))
    
# Requirement: Get Student Name & Number Of Courses he joined from student.json file
with open("03_file_management/student.json","r") as file_data:
    data = json.load(file_data)

print("Student Name: ",data['name'])
print("Student Joined Courses: ",len(data['courses']))
print("Student Second Course: ",data['courses'][1])

# dumps(): Serializes a Python object to a JSON-formatted string ("dump string").

student = {
    "id":"101",
    "name":"Ravi",
    "email":"ravi@gmail.com",
    "courses":["python","ai","cloud"],
    "gpa":9.5
}

print(type(student))

json_string = json.dumps(student)
print(type(json_string))
print("JSON Data",json_string)

# loads():Deserializes a JSON-formatted string to a Python object ("load string").
json_string = '{"id": "101", "name": "Ravi", "email": "ravi@gmail.com", "courses": ["python", "ai", "cloud"], "gpa": 9.5}'
print(type(json_string))

python_object = json.loads(json_string)
print(type(python_object))
print("Python Data",python_object)

print("=" * 50)

# Requirement: We have an API, when requested we are getting JSON Data 
# https://dummyjson.com/users

# Requirements: Find Number Of Users in the platform 

# pip install requests
import requests
api_endpoint = 'https://dummyjson.com/users'
response = requests.get(api_endpoint)
status_code = response.status_code
print("HTTP Status Code: ",status_code)

print("HTTP Response: ",response.text) # Response is in json string
print(type(response.text))

# Requirements: Find Number Of Users in the platform 
api_data_fetched = response.text
api_data_dict = json.loads(api_data_fetched)
print(api_data_dict)
print(type(api_data_dict))

# Requirements: Find Number Of Users in the platform 
all_users = api_data_dict['users']
print(all_users)
print(type(all_users))
print("=" * 100)
print("Current Number Of Users In Platform: ",len(all_users))
print("=" * 100)

# Requirements: Fetch All Users - usernames in the platform 
for user in all_users:
    # print(user)
    print(user['id'],user['username'])
    # print("=" * 30)
    
print("=" * 100)

# Requirements: Fetch All Users Who are Young i.e aged below 30 along with usernames and age in the platform 
print("=" * 30)
print("     Young Users In Platform")
print("=" * 30)
for user in all_users:
    if user['age'] < 30:
        print(user['id'],user['username'],user['age'])
    
print("=" * 100)
