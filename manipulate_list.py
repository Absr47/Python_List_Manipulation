# This program demonstrates several common list manipulation methods in Python.

def manipulate_list():
    """
    This function performs a series of operations on a list as requested.
    It prints the list at various stages to show the changes.
    """
    
    # 1. Create an empty list called my_list.
    my_list = []
    print(f"1. Initial empty list: {my_list}")
    
    # 2. Append the following elements to my_list: 10, 20, 30, 40.
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)
    print(f"2. After appending elements: {my_list}")
    
    # 3. Insert the value 15 at the second position (index 1) in the list.
    my_list.insert(1, 15)
    print(f"3. After inserting 15 at index 1: {my_list}")
    
    # 4. Extend my_list with another list: [50, 60, 70].
    my_list.extend([50, 60, 70])
    print(f"4. After extending with [50, 60, 70]: {my_list}")
    
    # 5. Remove the last element from my_list.
    my_list.pop() # pop() without an index removes the last element
    print(f"5. After removing the last element: {my_list}")
    
    # 6. Sort my_list in ascending order.
    my_list.sort()
    print(f"6. After sorting the list: {my_list}")
    
    # 7. Find and print the index of the value 30 in my_list.
    try:
        index_of_30 = my_list.index(30)
        print(f"7. The index of the value 30 is: {index_of_30}")
    except ValueError:
        print("7. The value 30 was not found in the list.")

# Run the function to execute the list operations.
if __name__ == "__main__":
    manipulate_list()

