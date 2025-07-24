class Meth:
    def __init__(self,x , y ):
        self.x = x
        self.y = y
    
    def __str__(self):
        return  f"{self.x}"

meth = Meth(2,3)
print(meth)


class Ops:

    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Ops(self.x + other.x, self.y * other.y )
    
    def __str__(self):
        return f"x = {self.x}, y = {self.y}"

    
ops1 = Ops(3, 5)
ops2 = Ops(4,89)

print(ops1 + ops2)
            
