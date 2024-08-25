def frist_occurance(array,target):
    low,high = 0, len(array) - 1
    first_occur = -1
    
    while low <= high:
        mid = (low+high) // 2
        
        if array[mid] == target:
            first_occur = mid
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_occur

def last_occurance(array,target):
    low, high = 0, len(array) -1
    last_occur = -1
    while low <= high:
        mid = (low+high)//2
        
        if array[mid] == target:
            last_occur = mid
            low = mid + 1
        elif array[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return last_occur
        
def find_occurance(array,target):
    first_occur = frist_occurance(array,target)
    last_occur = last_occurance(array,target)
    print(first_occur,last_occur)

array = [5,7,7,8,8,10]
find_occurance(array,5)