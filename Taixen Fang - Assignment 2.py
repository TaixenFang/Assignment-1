# Function 1: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):    # Defining the function
    unique_numbers = list(set(numbers))     # Sorting the numbers and removing the duplicates
    unique_numbers.sort()
    return unique_numbers
numbers = [12,15,20,9,7,7,4,129,150,129,-1,-1,-2,-2,-10,-20]    # My own list of numbers in a random order
print(remove_duplicates_and_sort(numbers))  # Function call


# Function 2: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):                    # Defining the function
    result = []                             # Empty list to store the cummulated sums
    total = 0                                   
    for i in arr:                           # For loop for each number
        total += i                          # Adding current number to total count
        result.append(total)                # Appending the sum to the result list
    return result
arr = [1,4,7,9,14,20]                       # Creating the array of numbers
print(cumulative_sum(arr))                  # Function call
    

# Function 3: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):                             # Defining the function
    return [lst[i] for i in range(step-1, len(lst), step)]  # Slicing the list at every Nth element
lst = [1,4,5,6,8,12,128,197]                                # List of random numbers
step = 2                                                    # Slicing step vaalue
print(slice_every_nth(lst, step))                           # Function call


# Function 4: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):              # Defining function
    result = 0                              # Initial result
    for i in range(len(list1)):             # For loop
        result += list1[i]*list2[i]         # Dot product calculation
    return result                           # Final result
list1 = [25,50,75]                          # Lists containing three random numbers each
list2 = [100,200,300]                   
print(dot_product(list1, list2))            # Function call


# Function 5: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]     # Empty result matrix; same number of rows as matrix 1 and same number of columns as matrix 2
    for i in range(len(matrix1)):                                                   # For loop for each row of matrix 1
        for j in range(len(matrix2[0])):                                            # For loop for each column of matrix 2
            for k in range(len(matrix2)):                                           # Looping through every element in matrix 1's row and matrix 2's column
                result[i][j] += matrix1[i][k] * matrix2[k][j]                       # Matrix multiplication
    return result
matrix1 = [         # Matrix filled with random numbers
    [1,2,3],
    [4,5,6]
]
matrix2 = [
    [19,20],
    [25,26],
    [29,30]
]
print(matrix_multiplication(matrix1, matrix2))  # Function call
