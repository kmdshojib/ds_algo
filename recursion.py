# def fib(n):
#     if n == 0: return 1
#     else: return n + fib(n-1)

# print(fib(6))

def powerOfTwo(n):
    if n < 1:
        return False
    if n == 1:
        return True
    if n % 3 == 0:
        return powerOfTwo(n//3)
    return False
print(powerOfTwo(27))