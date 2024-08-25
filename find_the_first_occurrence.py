def find_the_first_occurrence(arr,target):
    if not arr:
        return 0
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
            break
    return 0
arr = [1, 2, 2,3, 4,0, 5]
print(find_the_first_occurrence(arr,5))