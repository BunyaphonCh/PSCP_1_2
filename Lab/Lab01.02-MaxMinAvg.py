'''yeah'''
import json
def main():
    '''yeah'''
    n = input()
    lis = json.loads(n)
    most = 0
    low = 99999
    summ = 0
    for i in lis:
        if i > most:
            most = i
        if i < low:
            low = i
        summ += float(i)
    med = summ / len(lis)
    print(f'({most}, {low}, {med:.2f})')
main()
