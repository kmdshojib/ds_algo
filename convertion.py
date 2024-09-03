class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Create a list to store the numeric values of characters
        numbers = []
        result = 0
        
        # Traverse through each character in the string
        for c in s:
            numbers.append(ord(c) - 96)
    
        # Convert the list of numbers into a single string
        num_str = "".join(map(str, numbers))
        
        # calcluate the sum of the converted 
        for num in num_str:
            result = result + int(num)
        
        # If k is 1, return the result of the first transformation
        if k == 1:
            return result
        
        # Perform k-1 transformations where each transformation
        for _ in range(k - 1):
            result = sum(int(num) for num in str(result))
        
        return result
