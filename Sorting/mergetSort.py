def sortArray(self, nums: List[int]) -> List[int]:
    if len(nums) < 1:
            # deterimie the mid of array
        mid = len(nums) // 2
            # slice array into halvs
        nums_of_left = nums[:mid]
        nums_of_right =nums[mid:]

            # divide the arrays until you reach at postion 1
        self.sortArray(nums_of_right)
        self.sortArray(nums_of_left)

        i = j = k = 0
            # merge and sort divided part

         while i < len(nums_of_left) and j < len(nums_of_right):
            if nums_of_left[i] < nums_of_right[j]:
                nums[k] = nums_of_left[i]
                i+=1
            else:
                nums[k] = nums_of_right[j]
                j+=1
            k+=1
            
         while i < len(nums_of_left):
            nums[k] = nums_of_left[i]
            i+=1
            k+=1
        while j < len(nums_of_right):
            nums[k] = nums_of_right[j]
            j+=1
            k+=1
    return nums

arr = [5,2,3,1]
print(sortArray(arr))