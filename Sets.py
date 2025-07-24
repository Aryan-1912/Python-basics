my_set = {1,2,3,4,5,6,7,7,8,88,9,999,9999,999,5}
print(my_set)
print(type(my_set)) 

my_set.add("loda")
print(my_set)

my_set.discard(4)
print(my_set)

removed_element = my_set.pop()
print(removed_element)

print(my_set)