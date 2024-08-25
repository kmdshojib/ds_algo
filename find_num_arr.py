# Find a Number in an Array

# Problem: Given an array of integers and a target value, determine if the target value exists in the array. Return the index if found, otherwise return -1.
# Example Input: arr = [10, 23, 45, 70, 11, 15], target = 70
# Example Output: 3
# Edge Cases:
# Target is not present: arr = [10, 23, 45, 11, 15], target = 70 → Output: -1
# Empty array: arr = [], target = 5 → Output: -1

def find_num_in_array(array,target):
	n = len(array)
	for index in range(n):
		if arr[index]==target:
			return index
		# else:
		# why can't we return -1 here?
      	# 	return -1
	return -1

arr = [10, 23, 45, 70, 11, 15]
print(find_num_in_array(arr,70))