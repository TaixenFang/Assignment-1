# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3): #defining the function
    return max(num1, num2, num3) #checking max
num1 = float(input("Enter num1: ")) #user inputs
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))
print(built_in_functions_max(num1, num2, num3)) #function call


# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3): #defining the function
    return min(num1, num2, num3) #checking min
num1 = float(input("Enter num1: ")) #user inputs
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))
print(built_in_functions_min(num1, num2, num3)) #function call


# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number > 0: #set conditions
        return "The number is positive." #message
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is 0."
number = float(input("Enter the number: ")) #user input
print(check_number(number)) #function call


# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    for i in range(1, rows + 1): #for loop
        print("*" * i)
rows = int(input("Enter the number of rows: ")) #user input
star_shape(rows) #function call


# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    i = 1
    while i <= limit:
        if i % 3 == 0: #set conditions
            print("Multiplie of 3")
        else:
            print(i)
        i += 1
limit = int(input("Enter the limit: ")) #user input
count_multiples_of_3(limit) #function call


# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    for i in range(start, 1+end): #for loop
        if i % 2 == 0: #set even condition
            total += i
    return total
start = int(input("Enter the start of range: ")) #user inputs
end = int(input("Enter the end of range: "))
print(sum_of_even_numbers(start, end)) #function call