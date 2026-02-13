def summation(n):
    z = n - n
    a = n
    b = n + 1
    r = z
    
    while b > z:
        if b & 1:
            r = r + a
        a = a << 1
        b = b >> 1
        
    return r >> 1

num = int(input())
print(summation(num))