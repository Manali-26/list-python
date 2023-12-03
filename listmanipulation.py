# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print("Accessing elements:")
print(my_list[0])    # Output: 1
print(my_list[-1])   # Output: 5

# Slicing
print("\nSlicing:")
subset = my_list[1:4]  # Extract elements at index 1, 2, and 3
print(subset)         # Output: [2, 3, 4]

# Modifying elements
print("\nModifying elements:")
my_list[2] = 99
print(my_list)        # Output: [1, 2, 99, 4, 5]

# Adding elements
print("\nAdding elements:")
my_list.append(6)
print(my_list)        # Output: [1, 2, 99, 4, 5, 6]

my_list.insert(2, 100)
print(my_list)        # Output: [1, 2, 100, 99, 4, 5, 6]

# Removing elements
print("\nRemoving elements:")
my_list.remove(99)
print(my_list)        # Output: [1, 2, 100, 4, 5, 6]

popped_element = my_list.pop(2)
print(my_list)        # Output: [1, 2, 4, 5, 6]
print("Popped Element:", popped_element)  # Output: 100

# List concatenation
print("\nList concatenation:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# List comprehension
print("\nList comprehension:")
squared_numbers = [x**2 for x in range(1, 5)]
print(squared_numbers)  # Output: [1, 4, 9, 16]

