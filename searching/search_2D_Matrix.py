
def search_matrix(matrix,target):
    n = len(matrix)
    
    for i in range(n):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True
    return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_matrix(matrix,60))
