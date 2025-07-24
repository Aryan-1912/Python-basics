def func(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

func(4)
func(5)

def greet(name = "everyone"):
    print(f"{name} is fuckeddddd")

greet()


def print_3(*args):
    for number in args:
        print(number)
    
print_3(1,2,3,"hello",4,5,6)


def print_2(**kwargs):
    for keys, values in kwargs.items():
        print(f"{keys}:{values}")

print_2(name="Arayn", kmfdk="ewf")

def print_4(*args, **kwargs):
    for i in args:
        print(f"Posiiii args {i}")
    for keys, Values in kwargs.items():
        print(f"{keys}  -  {Values}")
print_4(1,2,3,4,5, name="aryan", age="43" )    

