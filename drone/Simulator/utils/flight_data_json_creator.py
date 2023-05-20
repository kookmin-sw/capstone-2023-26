import json
import random

data = []

for i in range(0, 120):#range(0, 65//5 + 1):
    seconds_str = f"{i * 5 % 60}".zfill(2)
    minutes_str = f"{i * 5 // 60}".zfill(2)

    pos_x = random.uniform(37.609965, 37.612793)
    pos_y = random.uniform(126.992861, 126.998341)

    # pos_x = round(37.61124 + (i * 0.02), 6)
    # pos_y = round(126.99648 + (i * 0.01), 6)

    voltage = round(12.04 - (i * 0.01), 2)

    item = {
        "id": i,
        "time": f"2023-05-08T13:{minutes_str}:{seconds_str}",
        "coordinate": [
            pos_x,
            pos_y
        ],
        "voltage": voltage,
        "event_id": i
    }
    data.append(item)

# .json 파일에 데이터 저장
with open("data.json", "w") as file:
    json.dump(data, file)
