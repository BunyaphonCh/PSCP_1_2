import json

def is_less_than(seat1, seat2):
    char1, num1 = seat1[0], int(seat1[1:])
    char2, num2 = seat2[0], int(seat2[1:])
    
    if char1 < char2:
        return True
    elif char1 == char2:
        return num1 < num2
    return False

def insertionSort(lst, last):
    comparison = 0
    for i in range(1, last + 1):
        current_value = lst[i]
        j = i - 1
        while j >= 0:
            comparison += 1
            if is_less_than(current_value, lst[j]):
                lst[j + 1] = lst[j]
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
