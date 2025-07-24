empty_tuples = ()
print(empty_tuples)
print(type(empty_tuples))

#list casted as tuple
num = tuple([1,2,3,4,5,6])
print(num)
print(type(num))

mix_tup = (1,"hello", 3.14)

#access elements in tup

print (mix_tup[2])

concatenation = mix_tup+num
print(concatenation)

print(concatenation*3)

print(concatenation.count(1))
print(concatenation.index(2))


packed_tup = 1,'jewjf', 95.00

print(packed_tup)

a, b, c = packed_tup
print(a)
print(b)

nest_tup = ([1,2,3], [4,5,6], [7,8,9])

for i in nest_tup:
    for j in i:
        print(j,"  ")
    print("")
