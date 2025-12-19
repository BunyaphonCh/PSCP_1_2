'''นรกขุมใหม่'''
def main():
    '''Ayo'''
    num = [int(input()) for _ in range(4)]
    num.remove(min(num))
    print(sum(num))
main()
