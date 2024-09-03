def chalk_replacer(chalk,k):
    total_chalk = sum(chalk)
    k %= total_chalk
    
    for i in range(len(chalk)):
        print("K: ",k)
        if k <= chalk[i]:
            return i
        k -= chalk[i]


chalk = [3,4,1,2]
k = 25

print(chalk_replacer(chalk,k))
# output: 0

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Step 1: Calculate the total chalk needed for one full round
        total_chalk = sum(chalk)
        # Step 2: Reduce k modulo total_chalk
        k %= total_chalk

        # iterate though array who can't find their turn 
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            
            # decrement k by chalk[i]

            k-=chalk[i]