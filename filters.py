



num = [
    {"name": "aryn", "age": 40},
    {"name": "ryan", "age": 50},
    {"name": "aran", "age": 40},
    {"name": "ayan", "age": 407}
]

def get_2(x):
    return x["age"] >=50 

y = list(filter(get_2, num))

print(y)