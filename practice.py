# # def pratision(arr,low,high):
# #     pivot = arr[high]
# #     i = low - 1
    
# #     for j in range(low,high):
        
# #         if arr[j] <= pivot:
# #             i += 1
# #             arr[i],arr[j] = arr[j],arr[i]
# #     arr[i+1],arr[high] = arr[high], arr[i+1]
# #     return i + 1

# # def quick_sort(arr,low,high):
# #     if low < high:
# #         pi = pratision(arr,low,high)
# #         print(pi)
# #         quick_sort(arr,low,pi-1)
# #         quick_sort(arr,pi+1,high)

# # arr = [64, 34, 25, 12, 22, 11, 90]
# # quick_sort(arr,0,len(arr)-1)
# # print(arr)

# def merge_sort(array):
#     if len(array) > 1:
        
#         mid = len(array) // 2
#         left_array = array[:mid]
#         right_array = array[mid:]
        
#         merge_sort(left_array)
#         merge_sort(right_array)
        
#         i = j = k = 0
        
#         while i < len(left_array) and j < len(right_array):
#             if left_array[i] < right_array[j]:
#                 array[k] = left_array[i]
#                 i+=1
#             else:
#                 array[k] = right_array[j]
#                 j+=1
#             k+=1
        
#         while i < len(left_array):
#             array[k] = left_array[i]
#             i+=1
#             k+=1
        
#         while j < len(right_array):
#             array[k] = right_array[j]
#             j+=1
#             k+=1
#     return array

# array = [10,3,99,33,56,1,9,0,4]
# array.sort(reverse = True)
# # print(merge_sort(array))

# print(array)

def find_in_matrix(matrix,target):
    
    for i in range(len(matrix)):
        
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True
    return False
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(find_in_matrix(matrix,5))