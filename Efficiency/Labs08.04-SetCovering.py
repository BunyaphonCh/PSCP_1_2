def findStations(city_need, stations):
    uncovered = set(city_need) # เเปลงค่าจาก list เป็น str เริ่มเเรกจะเป็นชื่อเมืองทั้งหมด
    selected = [] # เอาไว้ใส่สถานีที่จะเลือก
    remain = stations[:]
    while uncovered and remain: # loop จนกว่า uncovered จะว่าง
        best_idx = max(
            range(len(remain)),
            key=lambda i: len(set(remain[i]['Cities']) & uncovered)
        )
        best_coverage = len(set(remain[best_idx]['Cities']) & uncovered)
        if best_coverage == 0:
            break
        selected.append(remain[best_idx]['Name'])
        uncovered -= set(remain[best_idx]['Cities'])
        remain.pop(best_idx)
    return sorted(selected) # คืนค่าชื่อสถานีที่ครอบคลุม
    
def main():
    import json
    city = json.loads(input())
    num_station = int(input()) # รับจำนวนสถานีทั้งหมดที่มี
    stations = [json.loads(input()) for _ in range(num_station)] # เอาไว้เก็บค่าสถานี
    print(findStations(city, stations))
main()
