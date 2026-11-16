# External Modules 

# API - https://dummyjson.com/products

# Check API Status and Process 

# import requests # ModuleNotFoundError: No module named 'requests'
# response = requests.get('https://dummyjson.com/products')

# pip install requests (Run this on terminal)
import requests # ModuleNotFoundError: No module named 'requests'
response = requests.get('https://dummyjson.com/products')
status_code = response.status_code
print(status_code)

print("=" * 50)

response = requests.get('https://dummyjson.com/countries')
status_code = response.status_code
print(status_code)

print("=" * 50)

response = requests.get('https://dummyjson.com/countries')
response = requests.get('https://dummyjson.com/products')
status_code = response.status_code
# print(status_code)
if status_code == 200:
    print("Processing API Data..................")
else:
    print("Processing API Data Failed")
    
print("=" * 50)