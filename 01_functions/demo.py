# Arbitrary Positional Arguments 

# Without Arbitrary Positional Arguments 
def add_one_number(n1):
    print(n1)
    
def add_two_number(n1,n2):
    print(n1 + n2)

def add_five_number(n1,n2,n3,n4,n5):
    print(n1 + n2 + n3 + n4 + n5)
    
add_one_number(1)
print("=" * 50)
add_two_number(1,2)
print("=" * 50)
# add_three_number(1,2,3)
# print("=" * 50)
add_five_number(1,2,3,4,5)
print("=" * 50)

# With Arbitrary Positional Arguments 
def add_numbers(*numbers):
    print(numbers)
    
add_numbers(1)
print("=" * 50)
add_numbers(1,2)
print("=" * 50)
add_numbers(1,2,3)
print("=" * 50)
add_numbers(1,2,3,4,5,6,7)
print("=" * 50)


# With Arbitrary Positional Arguments 
def add_numbers(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    print(f"Total Sum is {total_sum}")
        
add_numbers(1)
print("=" * 50)
add_numbers(1,2)
print("=" * 50)
add_numbers(1,2,3)
print("=" * 50)
add_numbers(1,2,3,4,5,6,7)
print("=" * 50)

# Real World use Case - Ecommerce Cart 
def cart_total_value(*product_prices):
    total_cart = 0
    for price_product in product_prices:
        total_cart += price_product
    print(f"Total Cart Value {total_cart}")
    
# Customer One 
cart_total_value(399,499)

print("=" * 50)

# Customer Two 
cart_total_value(1599,799,7490,2699)