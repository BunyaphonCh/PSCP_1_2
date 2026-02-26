import json

def is_less_than(seat1, seat2):
    char1, num1 = seat1[0], int(seat1[1:])
    char2, num2 = seat2[0], int(seat2[1:])
    
    if char1 < char2:
        return True
    if char1 == char2:
        return num1 < num2
    return False

def bubbleSort(lst, last):
    comparison = 0
    for current in range(0, last + 1):
        is_swapped = False
        for i in range(last, current, -1):
            comparison += 1
            if is_less_than(lst[i], lst[i-1]):
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
