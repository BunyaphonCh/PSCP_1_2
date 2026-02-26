import json
def insertionSort(lst, last):
    comparison = 0
    for i in range(1, last + 1):
        current_value = lst[i]
        j = i - 1
        while j >= 0:
            comparison += 1
            if lst[j] > current_value:
                lst[j+1] = lst[j]
                j -= 1
            else:
                break
        lst[j + 1] = current_value
        print(lst)
    print("Comparison times:", comparison)
def main():
    data = json.loads(input())
    last_index = int(input())
    insertionSort(data, last_index)
main()