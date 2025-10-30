# Function 1: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):    # Defining the function
    redooo             # Sorting the numbers and removing the duplicates
numbers = [12,15,20,9,7,7,4,129,150,129,-1,-1,-2,-2,-10,-20]    # My own set of numbers in a random order
print(remove_duplicates_and_sort(numbers))  # Calling the function


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
print(cumulative_sum(arr))      # Calling the function
    

# Function 3: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):                             # Defining the function
    return [lst[i] for i in range(step-1, len(lst), step)]  # Slicing the list at every Nth element
lst = [1,4,5,6,8,12,128,197]
step = 2
print(slice_every_nth(lst, step))



# Function 4: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    return 0

# Function 5: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    return [[0, 0], [0, 0]]
