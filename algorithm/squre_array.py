def merge(num1,num2):
    
    for i in range(len(num2)):
        num1.append(num2[i])
    
    num1.sort()
    print(num1)
    
        
        

num1 = [1,2,3,4]
num2 = [2,3,4,5]

print(merge(num1,num2))