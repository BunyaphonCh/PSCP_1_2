import json

def coinExchange(amount, coins): # {"10": 10, "5": 10, "2": 10, "1": 10}
    print(f'Amount: {amount}') # 127
    keys = list(coins.keys()) # [10, 5, 2, 1]
    results = [] # เก็บคำตอบ
    left = amount # 127
    count = 0
    for key in keys: # 10, 5, 2, 1 
        available = coins[key] # ค่า value 10, 10, 10, 10
        use = min(int(left / key), available) # 127 / 10 vs 10 |
        left = left - (use * key) # 127 - (10 * 10) = 27 |
        results.append((key, use)) # 10, 10 |
        count += use # 10 |
    if left > 0: # ถ้าวนครบเเล้ว ค่ายังมากกว่า 0 อยู่ เเปลว่าเหรียญที่มีพอจะเเลกได้เป๊ะๆ
        print('Coins are not enough.')
    else:
        print('Coin exchange result:')
        for key, use in results: # วนลูปเเสดงผล
            print(f'  {key} baht = {use} coins')
        print(f'Number of coins: {count}')

def convert_key(data):
    return {int(k): v for k, v in data.items()}

def main():
    money = int(input())
    data = convert_key(json.loads(input()))
    coinExchange(money, data)
main()