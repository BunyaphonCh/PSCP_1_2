'''Lab 01.04 - Recursive GCD'''
def gcd(a, b):
    '''Lab 01.04 - Recursive GCD'''
    if b == 0:
        return a
    elif b > 0:
        return gcd(b, a%b)
num1 = int(input())
num2 = int(input())
print(gcd(num1,num2))
