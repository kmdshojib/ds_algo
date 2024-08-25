
def count_occurrences(array,target):
    count = 0
    if not array:
        return 0
    for i in range(len(array)):
        if(array[i] == target):
            count+=1
    return count
arr = [2, 3, 2, 4, 2, 5]
print(count_occurrences(arr,2))