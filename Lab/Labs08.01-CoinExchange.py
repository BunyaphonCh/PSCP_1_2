import json

def coinExchange(amount, coins):
    print(f'Amount: {amount}')
    keys = sorted(list(coins.keys()),reverse=True)
    values = sorted(list(coins.values()),reverse=True)
    count = 0
    use = 0
    cal = int(amount / keys[0])
    if cal > values[0]:
        use = values[0]
    else:
        use = cal
    count += use
    print('Coin exchange result:')
    print(f'  {keys[0]} baht = {values[0]} coins')
    next = amount - (use * keys[0])
    for i in range(1,len(keys)):
        cal = int(next / keys[i])
        if cal > values[i]:
            use = values[i]
        else:
            use = cal
        print(f'  {keys[i]} baht = {use} coins')
        count += use
        next = next - (use * keys[i])
    print(f'Number of coins: {count}')

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    money = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(money, data)
main()