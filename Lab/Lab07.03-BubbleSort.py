import json
def bubbleSort(lst, last):
    comparison = 0
    for current in range(0, last + 1):
        is_swapped = False
        for i in range(last, current, -1):
            comparison += 1
            if lst[i] < lst[i-1]:
                lst[i], lst[i-1] = lst[i-1], lst[i]
                is_swapped = True
        print(lst)
        if not is_swapped:
            break
    print("Comparison times:", comparison)

def main():
    data = json.loads(input())
    last_index = int(input())
    bubbleSort(data, last_index)
main()
