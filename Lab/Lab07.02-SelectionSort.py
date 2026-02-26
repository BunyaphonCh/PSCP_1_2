import json

def selectionSort(lst, last):
    comparison = 0
    for current in range(0, last):
        smallest_index = current
        for i in range(current + 1, last + 1):
            comparison += 1
            if lst[i] < lst[smallest_index]:
                smallest_index = i
        lst[current], lst[smallest_index] = lst[smallest_index], lst[current]
        print(lst)
    print("Comparison times:", comparison)
    
def main():
    data = json.loads(input())
    last_index = int(input())
    selectionSort(data, last_index)
main()