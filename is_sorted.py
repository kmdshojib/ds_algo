def is_sorted(array):
    n = len(array)
    
    for i in range(n - 1):
        if array[i] > array[i + 1]:
            return False
    
    return True

arr = [1, 2,2, 4,5,6, 5]
print(is_sorted(arr))  # This will print False because the array is not sorted.
