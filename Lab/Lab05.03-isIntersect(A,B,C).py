import json

def isIntersect(a, b, c):
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)
    
    for item in set_a:
        if item in set_b and item in set_c:
            return True
            
    return False

def main():
    list_a = json.loads(input())
    list_b = json.loads(input())
    list_c = json.loads(input())
    
    print(isIntersect(list_a, list_b, list_c))

main()