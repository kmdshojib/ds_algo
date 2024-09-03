# I'm give 1d array I need to convert it to 2D

# input = [1,2,3,4]
# output =[[1,2],[3,4]]
# m * n

def construct2DArray(array):
    
    if array is None:
        return []
    costruced = []
    
    for i in range(len(array)):
        
        costruced.append(array[i:2])
        
    return costruced

array = [1,2,3,4]

print(construct2DArray(array))
