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

