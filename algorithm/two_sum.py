def two_sum(nums,target):
    n = len(nums)
    if n == 2:
           if nums[0] + nums[1] == target:
                return [0,1]
    
    low, high = 0, n - 1
    while low <= high:
        
        sum = nums[low] + nums[high]
        
        if sum == target:
            return [low, high]
        elif sum < target:
            low+=1
        else:
            high-=1
    return None
            
nums = [3,2,4]
print(two_sum(nums, 6))cZ