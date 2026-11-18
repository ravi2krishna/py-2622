# Working With CSV Data / File 

# Read CSV Data 
with open("03_file_management/students.csv","r") as file_data:
    print(file_data.read())
    
print("=" * 50)
    
# Assume We Have 50k Student Records 
# Customer Requirement: There Will Be Job Drive In Hyderabad Location, Get Me Hyderabad Students Data 
with open("03_file_management/students.csv","r") as file_data:
    print(file_data.read().find("Hyderabad"))
    
print("=" * 50)

# Assume We Have 50k Student Records 
# Customer Requirement: There Will Be Job Drive In Hyderabad Location, Get Me Hyderabad Students Data 
import csv
with open("03_file_management/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    
    for row in csv_reader:
        print(row)
        # print(row[-1])
        if row[-1] == "Hyderabad":
            print(row)
    
print("=" * 50)

# Assume We Have 50k Student Records 
# Customer Requirement: There Will Be Job Drive In Hyderabad Location, 
# Get Me Hyderabad Students Data who took internship from tcs 
import csv
with open("03_file_management/students.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[-1] == "Hyderabad" and row[1].endswith("@tcs.com"):
            print(row)
    
print("=" * 50)

# Assume We Have 50k Student Records 
# Customer Requirement: There Will Be Job Drive In Hyderabad Location, Get Me Hyderabad Students Data 
import csv
with open("03_file_management/sample.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    
    for row in csv_reader:
        # print(row)
        # print(row[-1])
        if row[2] == "Hyderabad":
            print(row)
    
print("=" * 50)

# Assume We Have 50k Student Records 
# Customer Requirement: There Will Be Job Drive In Hyderabad Location, Get Me Hyderabad Students Data 
import csv
with open("03_file_management/sample.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    
    for row in csv_reader:
        # print(row)
        if row['address'] == "Hyderabad":
            print(row)
    
print("=" * 50)

# Assume We Have 50k Student Records 
# Customer Requirement: There Will Be Job Drive In Hyderabad Location, Get Me Hyderabad Students Data 
import csv
with open("03_file_management/students.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    
    for row in csv_reader:
        # print(row)
        if row['address'] == "Hyderabad":
            print(row)
    
print("=" * 50)

# Write Data To CSV File 
with open("03_file_management/emp.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['emp_name', 'emp_email', 'emp_mobile', 'emp_address'])
    csv_writer.writerow(['Ravi', 'ravi186@tcs.com', '9876055200', 'Bangalore'])

fieldnames = ['emp_name', 'emp_email', 'emp_mobile', 'emp_address']
with open("03_file_management/new.csv","w") as file_data:
    csv_writer = csv.DictWriter(file_data,fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'emp_name': 'Santosh', 'emp_email': 'santosh579@outlook.com', 'emp_mobile': '9718726887', 'emp_address': 'Hyderabad'})





