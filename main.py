import json
def intersact(a,b,c):
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)
    
    for item in set_a:
        if item in set(b) and item in set(c):
            return True
    return False
def main():
    lis_a = json.loads(input())
    lis_b = json.loads(input())
    lis_c = json.loads(input())
    print(intersact(lis_a, lis_b, lis_c))
main()