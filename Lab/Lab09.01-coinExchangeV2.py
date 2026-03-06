import json

def coinExchangeV2(amount, coins):
    print(f'Amount: {amount}')
    
    coin_values = sorted([int(k) for k in coins.keys()], reverse=True)
    coin_counts = {int(k): v for k, v in coins.items()}
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    choice = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coin_values:
            if i >= coin and dp[i - coin] != float('inf'):
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    choice[i] = coin
    
    if dp[amount] == float('inf'):
        print('Can not exchange.')
        return
    
    result = {coin: 0 for coin in coin_values}
    current = amount
    
    while current > 0:
        coin_used = choice[current]
        if coin_used == -1:
            print('Can not exchange.')
            return
        result[coin_used] += 1
        current -= coin_used
    
    valid = True
    for coin in coin_values:
        if result[coin] > coin_counts[coin]:
            valid = False
            break
    
    if not valid:
        print('Can not exchange.')
        return
    
    print('Coin exchange result:')
    total = 0
    for coin in coin_values:
        print(f'  {coin} baht = {result[coin]} coins')
        total += result[coin]
    print(f'Number of coins: {total}')

def main():
    amount = int(input())
    coins = json.loads(input())
    coinExchangeV2(amount, coins)

main()