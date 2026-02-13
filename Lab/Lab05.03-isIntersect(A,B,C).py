def isIntersect(a, b, c):
    d = {}
    
    for x in a:
        d[x] = 1
    
    for x in b:
        if x in d:
            d[x] = 2
    
    for x in c:
        if x in d and d[x] == 2:
            return True
    
    return False

input1 = list(map(int, input()[1:-1].split(',')))
input2 = list(map(int, input()[1:-1].split(',')))
input3 = list(map(int, input()[1:-1].split(',')))

print(isIntersect(input1, input2, input3))