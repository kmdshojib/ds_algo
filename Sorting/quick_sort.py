import time

def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]  # Swap the elements at indices i and j
    arr[i+1],arr[high] = arr[high], arr[i+1]   # Swap the pivot element with the element at index (i + 1)
    return i + 1 # Return the index of the pivot

def quick_sort(arr,low,high):
    if low < high:
        pi = partition(arr,low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
start_time = time.time()
quick_sort(arr, 0, len(arr) - 1)
end_time = time.time()
print("Sorted array:", arr)
print("Time taken: {:.6f} seconds".format(end_time - start_time))

