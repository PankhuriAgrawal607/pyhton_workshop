class car:
    def __init__(self,make,model):
        self.make=make
        self.model=model
car1=car("Toyota","Camry")
car2=car("Honda","Civic")
print(car1.make, car1.model)
print(car2.make, car2.model)