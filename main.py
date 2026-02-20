def count_presses(n):
    if n == 1:
        return 1
    total_digits = 0
    start = 1
    length = 1
    while start <= n:
        end = start * 10 - 1
        if end <= n:
            count = end - start + 1
            total_digits += length * count
        else:
            count = n - start + 1
            total_digits += length * count
        start *= 10
        length += 1
    return total_digits + n
def main():
    n = int(input())
    print(count_presses(n))
main()