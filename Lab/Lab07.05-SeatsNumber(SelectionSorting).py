import json
def is_less_than(seat1, seat2):
    char1, num1 = seat1[0], int(seat1[1:])
    char2, num2 = seat2[0], int(seat2[1:])
    if char1 < char2:
        return True
    if char1 == char2:
        return num1 < num2
    return False

def selectionSort(lst, last):
    comparison = 0
    for current in range(0, last):
        smallest_index = current
        for i in range(current + 1, last + 1):
            comparison += 1
            if is_less_than(lst[i], lst[smallest_index]):
                smallest_index = i
        lst[current], lst[smallest_index] = lst[smallest_index], lst[current]
        print(lst)
    print("Comparison times:", comparison)
    
def main():
    data = json.loads(input())
    last_index = int(input())
    selectionSort(data, last_index)
main()