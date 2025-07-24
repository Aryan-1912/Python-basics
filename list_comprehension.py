lst= [x**2 for x in range(10)]
print(lst)

# lst comprehension in you can perform iterartion aswell ass operations in list and can get the desired outout
# syntax
# lst = [expression for item in iterable]
# with condition the suntax is 
# lst = [expression for item in iterable if condition]
#nested list comprehension
# lst = [expression for item1 in iterable1 for item2 in iterable2 ]


lst1 = [x**2 for x in range(10) if x%2 == 0]
print (lst1)


lstn = [1,2,3]
lsta = ['a','b','c']

pair = [(i,j) for i in lstn for j in lsta]
print (pair)


words = ["aryan", "popat","paraararar"]
lengths = [len(word)for word in words]
print (lengths)