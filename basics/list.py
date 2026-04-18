# What are Lists?
# -------------------------------
#  Lists are sequence data types in Python that can store multiple values in a single variable.
#  Lists are mutable (modifiable) and can hold elements of different types (int, float, str, etc.)
#  They are similar to arrays but more flexible.

# Creating an empty list
my_list = []
a=["amdfd",2,'dad',2.09]
print(a)

# -------------------------------
# Accessing Elements from a List
# -------------------------------

x = [45, 43, 2, 1, 345, 5, 3]

print(x[2])       # Output: 2 (3rd element, index starts from 0)
print(len(x))     # Output: 7
print(x[-7])      # Output: 3 (last element using negative indexing)
print(type(x[2])) # Output: <class 'int'>

# IndexError Examples
# Uncommenting below will throw an error
# print(x[-10])   # IndexError: list index out of range
# print(x[100])   # IndexError: list index out of range


# -------------------------------
# Iterating Through a List
# -------------------------------

# 1. By index

b=[1,2,5,43,2,7,9]

for i in range (len(b)):
    print(b[i])

print(*b) #In one line

# 2. By value

for value in b:
    print(value,end=" ")
    
# -------------------------------
# Built-in List Functions
# -------------------------------
a = [1, 2, 4, 55, 6, 6, 6, 6]

print("Sum : ",sum(a))
print("len : ",len(a))
print("len : ",min(a))
print("len : ",max(a))

a.remove(1)

print(*a)

a.pop(6)

print(a)

# What is Slicing?
# Slicing means extracting a part of the list using the syntax:
# list[start:end:step]

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# 1. Basic slicing
print(nums[0:5])   # [10, 20, 30, 40, 50]
print(nums[:4])    # [10, 20, 30, 40]
print(nums[5:])    # [60, 70, 80, 90, 100]

# 2. Step slicing
print(nums[::2])   # [10, 30, 50, 70, 90] list[start : stop : step]
print(nums[1::2])  # [20, 40, 60, 80, 100]

# 3. Negative slicing (reverse)
print(nums[::-1])  # [100, 90, ..., 10]
print(nums[-3:])   # [80, 90, 100]
print(nums[-5:-2]) # [60, 70, 80]

# Why use slicing?
#  For data cleaning, data extraction, reversing lists, skipping elements, or efficient subsetting

# -------------------------------
# Final Summary
# -------------------------------
#  Lists are essential for managing and manipulating sequences of data.
#  Use methods like append, insert, pop, etc., to modify them.
#  Use list comprehensions for fast, readable logic.
#  Use slicing for powerful subsetting and transformations.

print(nums*2)

result_multiple_eachElement=[x*2 for x in nums]
print(result_multiple_eachElement)