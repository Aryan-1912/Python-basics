

numbers = [1,2,3,4,5]

sqa = list(map(lambda x: x*x, numbers)) 

print(sqa)

num1 = [1,2,3]
num2 = [1,2,3]

added = list(map(lambda x,y: x+y, num1,num2))

print(added)


def get_name(person):
    return person["name"]

people = [
    {"name": "aryan", "age": 40},
    {"name": "ayushiiii"}
]

result = list(map(get_name, people))
print(result)


