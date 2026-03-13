import json

def knapsackV2(capacity, items):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, value, weight = items[i-1]
        for w in range(capacity + 1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight] + value)
            else:
                dp[i][w] = dp[i-1][w]
                
    selected_items = []
    current_w = capacity
    for i in range(n, 0, -1):
        if dp[i][current_w] != dp[i-1][current_w]:
            item = items[i-1]
            selected_items.append(item)
            current_w -= item[2]
            
    selected_items.sort(key=lambda x: x[0])
    
    print(f"Total: {dp[n][capacity]}")
    for name, value, weight in selected_items:
        print(f"{name} -> {weight} kg -> {value} THB")

def main():
    raw_input1 = input().strip()
    raw_input2 = input().strip()

    if raw_input1.startswith('['):
        items = json.loads(raw_input1)
        capacity = int(raw_input2)
    else:
        capacity = int(raw_input1)
        items = json.loads(raw_input2)
        
    knapsackV2(capacity, items)

if __name__ == "__main__":
    main()