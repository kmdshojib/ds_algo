def bubble_sort(array):
    n = len(array)
    
    for i in range(n-1): # loop runs till O(n) times
        for j in range(n-i-1): # loop runs till O(n) times
            if array[j] > array[j+1]:
                #swap values
                array[j],array[j+1] = array[j+1],array[j]
    return array

array = [65,34,55,90]

print(bubble_sort(array))

# best case time complexity O(n)
# avgerage case time complexity O(n^2)
# worst case time complexity O(n^2)