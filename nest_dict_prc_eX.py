student = {
            "student1":{"name": "aryan", "age": 21},
            "student2":{"name": "chotu", "age": 21}
}

print(student)

print(student["student1"]["age"])
print(student["student1"]["name"])

for students_id, students_info in student.items():
    print(f"{students_id} and {students_info}")


# even as well as cube// use dict comprehension
cube = {x : x**3 for x in range (60) if x%2==0}
print(cube)



num = [1, 2,2, 3,3,3, 4,4,4,4]

freq={}

for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        
print(freq)




# merge 2 dict_


stud1 = {"name": " aryan ", "last": "prajapati", "age": 21}
tud = {"name": " ary ", "last": "pra", "age": 1}

dist= {**stud1, **tud}
print(dist)

for keys, values in stud1.items():
    print(f"---{keys}:----{values}")

