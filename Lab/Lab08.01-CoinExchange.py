'''
Steps
1. เเสดงค่า Amount ก่อน
2. สร้างตัวเเปร
3. สร้าง loop เช็คทุกค่าเเล้วเก็บใน list
4. ถ้าวนครบทุกตัวเเล้ว ยังเหลือค่ามากกว่า 0 เเปลว่าเหรียญที่มีบ่พอเเลก
5. ถ้าเเลกได้ ก็วนเเสดงค่าจากใน list ที่เก็บไว้
6. เเสดงจำนวนเหรียญทั้งหมดที่ใช้

Math
1. ยอดเงินทั้งหมดที่ต้องการเเลกเป็นเหรียญ / เหรียญที่ต้องการเเลก (เช่น เหรียญ 10)
2. เช็คว่าไอ้ค่าที่ได้ในข้อ 1 มันมากกว่าจำนวนเหรียญนั้นๆที่เรามีไหม
3. ถ้ามันมากกว่าก็ให้เอาจำนวนเท่าค่าเหรียญที่มีอยู่ (มีเหรียญจำนวนน้อยกว่าที่เเลกได้) ถ้าไม่ก็ใช้ค่าที่คำนวณเลย
4. เอาค่าที่คำนวณ คูณ ประเภทเหรียญ
5. เอาค่าที่เหลือ(ครั้งเเรกให้มีค่าเท่า Amount) ลบกับ ค่าที่คำนวณในข้อ 4 เป็นจำนวนเงินที่เหลือ ต้องเอาไปคิดต่อ
6. วนเรื่อยๆ ละก็บวกค่าจำนวนเหรียญไปด้วย
'''

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