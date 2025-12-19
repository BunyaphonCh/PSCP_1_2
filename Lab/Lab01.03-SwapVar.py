'''Lab 01.03 - SwapVar'''
def main():
    '''Lab 01.03 - SwapVar'''
    n = input()
    values = n.strip('()').split(', ')
    print(tuple(map(float, values[::-1])))
main()
