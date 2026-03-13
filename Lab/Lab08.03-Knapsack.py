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
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_weight(self):
        return self.weight
    def get_cost(self):
        return self.price
def value_per_weight(item):
    return item.price / item.weight # อัตราส่วนราคา หาร น้ำหนัก
def knapsack(itemList, amount):
    print(f'Knapsack Size: {amount:.1f} kg') # ขนาดที่กระเป๋าจุได้
    print('===============================')
    sorted_items = sorted(itemList, key=value_per_weight, reverse=True) # วนเก็บค่าอัตราส่วนทีละ item จนกว่าจะครบ เรียงจากมากไปน้อย
    selected = [] # เอาไว้เก็บค่า
    remain_weight = amount # เอาไว้เช็คว่าที่ยังเหลือพอให้ใส่อีกได้ไหม
    res = 0 # นับจำนวนเงินจากของที่ใส่ในปลาเก๋า
    for item in sorted_items:
        if remain_weight >= item.weight: # ถ้าพื้นที่ปลาเก๋ายังเหลือก็เข้าเงื่อนไข
            selected.append(item) # เก็บค่าอัตราส่วนที่ได้
            remain_weight -= item.weight # ลดน้ำหนักที่ใส่ได้ ตามของที่ใส่ลงปลาเก๋าไปเเล้ว
            print(f'{item.name} -> {item.weight} kg -> {item.price} THB')
            res += item.price # เพิ่มราคาของที่ใส่ลงปลาเก๋า
    print(f'Total: {res} THB')

def main():
    import json
    items = []
    num_items = int(input()) # จำนวนของที่หยิบ
    while num_items != 0:
        item_in = json.loads(input()) # รับค่าสิ่งที่หยิบ -> name, price, weight
        items.append(Item(item_in['name'], item_in['price'], item_in['weight'])) # เก็บข้อมูล value ลงใน list
        num_items = num_items - 1
    knapsack_capacity = float(input()) # น้ำหนักที่กระเป๋ารับรองได้
    knapsack(items, knapsack_capacity) # ค่าของสิ่งที่หยิบ, ค่าที่จุได้
main()
