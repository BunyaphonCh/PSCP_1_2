'''ไม่ได้สร้าง attribute เเต่ไปดึงตรง main เเทนเลย'''

class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

def main():
    import json
    item_in = json.loads(input())
    item = Item(item_in['name'], item_in['price'], item_in['weight'])
    print(item.name, item.price, item.weight, sep='\n')
main()