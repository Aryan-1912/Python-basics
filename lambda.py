def add(x,y):
    return x+y

print(add(1,2))


add1 = lambda c,b: c+b
print(add1(3,4))


lst = [1,2,3]

def sq(lst):
    total = 0 
    for ech_el in lst:
        total+=ech_el**2
    return total

print (sq(lst))




