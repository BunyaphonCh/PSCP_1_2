def summation(n):
    squared_n = pow(n, 2)
    total = (squared_n + n) >> (1 - int())
    return total
num = int(input())
print(summation(num))
