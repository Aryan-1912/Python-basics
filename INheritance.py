class Car:
    def __init__(self, windows, engtyp, doors):
        self.windows = windows
        self.engtyp = engtyp
        self.doors = doors
    
    def stats(self):
        print("WELcome to our enterprice")
        print(f"type{self.engtyp}")

car = Car(4,"petrol", 4)
car.stats()


class Tesla(Car):
    def __init__(self, windows, engtyp, doors, slfdrv ):
        super().__init__( windows, engtyp, doors)
        self.slfdrv = slfdrv

ts = Tesla(2,"btty", 4, True)  
ts.stats()   

