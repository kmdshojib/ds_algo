def negetive_num(nums):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] < 0:
            low = mid + 1
        else:
            high = mid - 1
            
    return low

def positive_num(nums):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] > 0:
            high = mid - 1
        else:
            low = mid + 1
            
    return len(nums) - low

def count_max(nums):
    # Handle edge case where all elements are zero
    if nums[0] == 0 and nums[-1] == 0:
        return 0
    
    # Handle edge case where all elements are positive
    if nums[0] > 0:
        return len(nums)
    
    # Handle edge case where all elements are negative
    if nums[-1] < 0:
        return len(nums)
    
    # General case: Count positive and negative numbers
    negetive_count = negetive_num(nums)
    positive_count = positive_num(nums)
    
    return max(positive_count, negetive_count)

# Test cases
nums1 = [-2, -1, -1, 0, 0, 0]
nums2 = [0, 0, 0, 1, 2, 3, 4]

print(count_max(nums1))  # Expected output: 3 (count of negative numbers)
print(count_max(nums2))  # Expected output: 4 (count of positive numbers)
