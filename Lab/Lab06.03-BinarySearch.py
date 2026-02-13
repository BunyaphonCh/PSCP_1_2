import json

def binary_search(data, target_name):
    low = 0
    high = len(data) - 1
    comparisons = 0
    found = False

    while low <= high:
        mid = (low + high) // 2
        
        comparisons += 1
        
        current_name = data[mid]['name']

        if current_name == target_name:
            print(f"Found {target_name} at index {mid}")
            print(f"ID: {data[mid]['id']}")
            print(f"Name: {data[mid]['name']}")
            print(f"GPA: {data[mid]['gpa']}")
            print(f"Comparisons times: {comparisons}")
            found = True
            break
        
        if target_name < current_name:
            high = mid - 1
        else:
            low = mid + 1

    if not found:
        print(f"{target_name} does not exists.")
        print(f"Comparisons times: {comparisons}")

def main():
    data_input = json.loads(input())
    
    search_name = input()
    
    binary_search(data_input, search_name)

if __name__ == "__main__":
    main()