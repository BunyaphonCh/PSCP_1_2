def find_longest_common_substring():
    string_a = input().strip()
    string_b = input().strip()
    
    n = len(string_a)
    longest_substring = ""
    max_length = 0
    
    for i in range(n):
        if n - i <= max_length:
            break
            
        current_length = max_length + 1
        while i + current_length <= n:
            substring = string_a[i : i + current_length]
            
            if substring in string_b:
                max_length = current_length
                longest_substring = substring
                current_length += 1
            else:
                break
                
    if max_length > 0:
        print(longest_substring)
        print(max_length)
    else:
        print("No common substring.")

if __name__ == "__main__":
    find_longest_common_substring()