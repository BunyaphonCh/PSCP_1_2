import json

def coinExchange(amount, coins):
    print(f'Amount: {amount}')
    results = []
    left = amount
    count = 0
    
    for key in sorted(coins.keys(), reverse=True): # เรียงละก็ loop เลยทีเดียว
        available = coins[key]
        use = min(left // key, available) # ใช้ // เร็วกว่า int() -> เป็นตัวเลข + ปัดเศษลงเหมือนกัน
        left -= use * key
        results.append((key, use))
        count += use
    if left > 0:
        print('Coins are not enough.')
    else:
        print('Coin exchange result:')
        for key, use in results:
            print(f'  {key} baht = {use} coins')
        print(f'Number of coins: {count}')

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    money = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(money, data)
main()