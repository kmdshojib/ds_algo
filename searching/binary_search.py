def binary_search(array, target):
    # Get the length of the array
    n = len(array)
    
    # Initialize the low and high pointers
    low = 0
    high = n - 1  # high should be n-1 because array indices are from 0 to n-1
    
    # Start the binary search loop
    while low <= high:
        # Calculate the mid index
        mid = (low + high) // 2
        print(f"Checking the middle element at index {mid}, which is {array[mid]}")
        
        # Check if the target is at the mid position
        if target == array[mid]:
            print(f"Target found at index {mid}")
            return mid  # Return the index of the target element
        
        # If the target is greater, ignore the left half
        elif target > array[mid]:
            print(f"Target is greater than {array[mid]}, moving right")
            low = mid + 1
        
        # If the target is smaller, ignore the right half
        else:
            print(f"Target is smaller than {array[mid]}, moving left")
            high = mid - 1
    
    # Target was not found in the array
    print("Target not found in the array")
    return -1

# Test the binary_search function
array = [1, 3, 4, 5, 6]
print(binary_search(array, 4))

# Time Complexity: O(log n)
# The algorithm repeatedly divides the search interval in half. 
# With each step, the number of elements to search is reduced by half, 
# leading to a logarithmic time complexity relative to the number of elements in the array.

# Space Complexity: O(1)
# The algorithm uses a constant amount of additional space, 
# regardless of the size of the input array. Only a few variables (low, high, mid) are used.
