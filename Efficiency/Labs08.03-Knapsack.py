'''
Goal : หยิบของให้ได้มากที่สุด โดยที่ไม่เกินน้ำหนักที่กระเป๋าจุได้

Steps
1. คำนวณราคา ต่อ น้ำหนัก = price / weight
2. เรียง items จากมาก ไป น้อย ตามค่าที่คำนวณได้
3. ถ้าค่าที่คำนวณได้เท่ากัน ให้เรียงตามตัวเเรกที่เข้ามาก่อน
4. หยิบของจนกว่าจะน้ำหนักเต็ม
'''
class Item:
    def __init__(self,name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def knapsack(itemList, amount):
    print(f'Knapsack Size: {amount:.1f} kg') # ขนาดที่กระเป๋าจุได้
    print('=' * 31)
    sorted_items = sorted(itemList, key=lambda x: x.price/x.weight, reverse=True) # วนเก็บค่าอัตราส่วนทีละ item จนกว่าจะครบ เรียงจากมากไปน้อย
    remain_weight = amount # เอาไว้เช็คว่าที่ยังเหลือพอให้ใส่อีกได้ไหม
    total = 0 # นับจำนวนเงินจากของที่ใส่ในปลาเก๋า
    for item in sorted_items:
        if remain_weight >= item.weight: # ถ้าพื้นที่ปลาเก๋ายังเหลือก็เข้าเงื่อนไข
            remain_weight -= item.weight # ลดน้ำหนักที่ใส่ได้ ตามของที่ใส่ลงปลาเก๋าไปเเล้ว
            print(f'{item.name} -> {item.weight} kg -> {item.price} THB')
            total += item.price # เพิ่มราคาของที่ใส่ลงปลาเก๋า
    print(f'Total: {total} THB')

def main():
    import json
    items = []
    num_items = int(input()) # จำนวนของที่หยิบ
    for _ in range(num_items):
        data = json.loads(input())
        items.append(Item(data['name'], data['price'], data['weight']))
    knapsack_capacity = float(input()) # น้ำหนักที่กระเป๋ารับรองได้
    knapsack(items, knapsack_capacity) # ค่าของสิ่งที่หยิบ, ค่าที่จุได้
main()
