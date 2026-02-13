def countPress(n):
    if n == 1:
        return 1
    
    digit = 0
    i = 1
    
    while i <= n:
        last = min(n, i*10 - 1)
        digit += (last - i + 1) * len(str(i))
        i *= 10
    
    return digit + (n-1) + 1

num = int(input())
print(countPress(num))
