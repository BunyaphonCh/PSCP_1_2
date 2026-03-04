'''
Goal : เลือกสถานีวิทยุให้น้อยที่สุด เเต่ครอบครุม เมืองทั้งหมด

Steps
1. สร้าง set ของเมืองที่ยังไม่ครอบ ตอนเริ่มจะใส่ทุกเมือง
2. สร้าง list เก็บสถานีที่เลือก
3. ลูปจนกว่า set ที่มีชื่อเมืองทั้งหมดจะว่าง
4. โดยจะหาสถานีที่ครอบเมืองมากที่สุด
5. ถ้าไม่มีสถานีไหนครอบเลย -> break
6. ถ้าเลือกสถานีนั้นก็เพิ่มเข้า list
7. ลบสถานีที่ครอบเเล้วออก
8. เเสดงผลเป็น list เเล้วเรียง (A-Z)
'''
def findStations(city_need, stations):
    uncovered = set(city_need) # เเปลงค่าจาก list เป็น str เริ่มเเรกจะเป็นชื่อเมืองทั้งหมด
    selected = [] # เอาไว้ใส่สถานีที่จะเลือก
    while uncovered: # loop จนกว่า uncovered จะว่าง
        best_station = None # สถานีที่เมืองครอบคุมมากที่สุด
        best_coverage = 0 # จำนวนเมืองที่สถานีครอบคลุมมากที่สุด
        for station in stations:
            coverage = len(set(station['Cities']) & uncovered) # จำนวนเมืองที่สถานีครอบคลุมเเล้ว เเละ ยังไม่ครอบคลุม
            if coverage > best_coverage: # ถ้าเจอสถานีใหม่ที่ครอบคลุมกว่าที่เก่าก็เอาค่าที่เจอ เท่ากับ ค่า best
                best_coverage = coverage
                best_station = station
        if best_station is None: # ถ้าไม่เจอสถานีไหนที่ครอบคลุมเลย ก็ออกจาก loop
            break
        selected.append(best_station['Name']) # ใส่ชื่อสถานีที่ครอบคลุมทั้งหมดใส่ลงใน list
        uncovered -= set(best_station['Cities']) # ลบเมืองที่สถานีนั้นครอบคลุมออก
    return sorted(selected) # คืนค่าชื่อสถานีที่ครอบคลุม
    
def main():
    import json
    city_str = input() # รับชื่อสถานทั้งหมด
    city_need = json.loads(city_str) # เเปลงค่าจาก str เป็น list
    num_station = int(input()) # รับจำนวนสถานีทั้งหมดที่มี
    station = [] # เอาไว้เก็บค่าสถานี
    for _ in range(num_station): # วนค่าตามจำนวนสถานี
        station_info = json.loads(input()) # รับค่าข้อมูลเเต่ละสถานี โดยเก็บเป็น list
        station.append(station_info) # เก็บข้อมูลลงใน list
    print(findStations(city_need, station))
main()
