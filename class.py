class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def start(self):
        print(f"{self.brand},{self.color} is running")
car1=Car("Toyota","Blue")
car2=Car("Mastang","Red")
class Car2:
    def __init__(self,engine,power):
        self.engine=engine
        self.power=power
    def start_2(self):
        print(f"{self.engine},{self.power} BHP")
car3=Car2('hundai',12)
car4=Car2('konami',15)
car1.start()
car2.start()
car3.start_2()
car4.start_2()