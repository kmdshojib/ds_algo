def find_the_last_occurrence(arr,target):
    # find the lass occurance
    occurance_count = -1
    if not arr:
        return -1
    for i in range(len(arr)):
        if arr[i] == target:
            occurance_count = i
    return occurance_count
arr = [8, 7, 5, 3,3]
print(find_the_last_occurrence(arr,3))