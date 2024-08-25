def searchInsertPortion(nums, target):
    low, high = 0, len(nums) - 1
    ans = len(nums)  # Default answer is the length of the list (end of the list)
    
    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        print(f"low: {low}, high: {high}, mid: {mid}, nums[mid]: {nums[mid]}")
        
        if nums[mid] >= target:
            ans = mid  # Potential insertion point found
            print(f"nums[mid] >= target, updating ans to {ans}")
            high = mid - 1  # Move to the left half to find the first possible insertion point
        else:
            low = mid + 1  # Move to the right half
            print(f"nums[mid] < target, updating low to {low}")
    
    print(f"Final insertion index: {ans}")
    return ans

nums = [1, 3, 5, 6]
print("Result:", searchInsertPortion(nums, 7))
