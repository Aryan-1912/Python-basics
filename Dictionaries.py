#empty_dict= {}
#print(empty_dict)
#print(type(empty_dict))

student = {"name": "Aryan",  "age": 34,  "grade": 'A'}
print (student)
print(student.keys())
print(student.values())
print(student.items())
print(student["grade"])
# another way to access elements in dict

print(student.get("grade"))

print(student.get("lastname" "Prajapati"))

student["grade"]= 'c'
print(student)

student["add"]= "A/4 502 nven dr"
print(student)

del student["age"]
print(student)


for keys in student.keys():
    print(keys)

for values in student.values():
    print(values)

for items in student.items():
    print(items)


for keys,values in student.items():
    print(f"-{keys} :: {values}")