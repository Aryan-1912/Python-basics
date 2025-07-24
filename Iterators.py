lst = [1,2,3,4,5]

iterator = iter(lst)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("chtkiiii gyu loda pati gyu pic")
