set = {1,2, 3, 4, 5}
print(3 in set)
print(11 in set)

set1 = {4,5}
set2 = {3,4,5,6,7,8,9}

print(set1.union(set2)) # gives combine
print(set1.intersection(set2)) # gives common
print(set1.intersection_update(set2))
print(set1)
set1 = {5}
print(set1.difference(set2))


print(set1.issubset(set2))
