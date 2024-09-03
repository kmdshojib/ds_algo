# def two_sum(nums, k):
#     left = 0
#     right = len(nums) - 1
#     nums.sort()
    
#     while left < right:
#         sum = nums[left] + nums[right]
#         if sum == k:
#             return [left, right]
#         elif sum < k:
#             left += 1
#         else:
#             right -= 1
    
#     return None

# nums = [3, 2, 4]
# print(two_sum(nums, 6))

# def two_sum(arr,target):
#     n = len(arr)
    
#     for i in range(n-1):
#         j = i+1
#         sum = arr[i] + arr[j]
#         print(sum)
#         print(j,j)
#         if sum == target:
#             return [i, j]

# nums = [3,2,3]
# print(two_sum(nums, 6))

def remove_duplicates(array):
    
    if not array:
        return 0
    
    i = 0
    
    for  j in range(1, len(array)):
        
        if arr[i] != arr[j]:
            i+=1
            arr[i] = arr[j]
    return array

arr = [10,10,11,12,14]
remove_duplicates(arr)
print(arr)