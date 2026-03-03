import json

def coinExchange(amount, coins):
    print(f'Amount: {amount}')
    # keys = sorted(list(coins.keys()),reverse=True)
    keys = list(coins.keys())
    values = list(coins.values())
    print(keys)
    print('fuc')
    cal = int(amount / keys[0])
    count = 0
    if cal > values[0]:
        cal = values[0]
    all = cal * keys[0]
    left = amount - all
    count += cal
    print('Coin exchange result:')
    print(f'  {keys[0]} baht = {cal} coins')
    for i in range(1,len(keys)):
        cal2 = int(left / keys[i])
        if cal2 > values[i]:
            cal2 = values[i]
        all = cal2 * keys[i]
        left = left - all
        if left < 0:
            print('Coins are not enough.')
            break
        count += cal2
        print(f'  {keys[i]} baht = {cal2} coins')
        if left == 0:
            break
    print(f'Number of coins: {count}')

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    money = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(money, data)
main()