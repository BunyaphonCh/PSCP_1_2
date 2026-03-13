'''
1. สร้าง class
2. สร้าง __init__ กำหนด attribute โดยใช้ self.x = x
3. สร้าง method get บลาๆ อย่าลืมใส่ parameter self กับต้อง return'''

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

def main():
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')
main()
