# Program to count the occurrences of a specific element in a list

# Taking a list of elements and the specific element as input from the user
elements = input("Enter a list of elements separated by spaces: ").split()
element_to_count = input("Enter the element to count: ")

# Counting the occurrences of the specific element
count = elements.count(element_to_count)

# Printing the count
print(f"The element '{element_to_count}' occurs {count} times in the list.")
