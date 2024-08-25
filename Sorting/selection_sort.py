def selection_sort(array):
    n = len(array)
    
    # run loop till the n-1 times and get the samllest elemrnt
    
    for i in range(n-1):
        smallest = i
        
        # find the smallest index
        for j in range(i+1, n):
            if array[smallest] > array[j]:
                smallest = j
        
        array[smallest] , array[i] = array[i],array[smallest]
    return array

array = [9, 3, 6, 8, 6, 0, 0]

sorted_array = selection_sort(array)
print("Sorted array is:", sorted_array)