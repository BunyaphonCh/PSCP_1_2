import json

def knapsackV2(items, capacity):
    n = len(items)
    
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, price, weight = items[i - 1]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            
            if w >= weight:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + price)
    
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name, price, weight = items[i - 1]
            selected.append((name, weight, price))
            w -= weight
    
    selected.sort(key=lambda x: x[0])
    
    total = dp[n][capacity]
    print(f'Total: {total}')
    for name, weight, price in selected:
        print(f'{name} -> {weight} kg -> {price} THB')

def main():
    items_input = json.loads(input())
    capacity = int(input())
    
    items = [(item[0], item[1], item[2]) for item in items_input]
    
    knapsackV2(items, capacity)

main()