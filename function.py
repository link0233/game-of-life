import json

def create_map(x,y):
    Map = []
    with open("./map/map.json",'r') as f:
        data = json.load(f)
    if data['map'] == "create":
        for i in range(y):
            line = []
            for j  in range(x):
                line.append(False)
            Map.append(line)
    else:
        Map = data["map"]

    return Map

def save(Map):
    data = {
        'map':Map
    }
    with open("./map/map.json","w") as f:
        json.dump(data,f)