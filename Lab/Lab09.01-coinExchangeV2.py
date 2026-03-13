import json

def main():
    amount = int(input())
    coins_dict = json.loads(input())
    
    coin_values = sorted([int(k) for k in coins_dict.keys()], reverse=True)

    dp = {0: (0,) * len(coin_values)}

    for j, v in enumerate(coin_values):
        limit = int(coins_dict[str(v)])
        for i in sorted(dp.keys(), reverse=True):
            for k in range(1, limit + 1):
                nxt = i + k * v
                if nxt > amount: 
                    break
                
                new_counts = list(dp[i])
                new_counts[j] += k
                new_res = tuple(new_counts)
                
                if nxt not in dp or sum(new_res) < sum(dp[nxt]) or (sum(new_res) == sum(dp[nxt]) and new_res > dp[nxt]):
                    dp[nxt] = new_res

    print(f"Amount: {amount}")
    if amount not in dp:
        print("Can not exchange.")
    else:
        print("Coin exchange result:")
        res = dp[amount]
        for val, count in zip(coin_values, res):
            print(f"  {val} baht = {count} coins")
        print(f"Number of coins: {sum(res)}")

main()