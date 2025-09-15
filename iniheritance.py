class Fardin:
    def __init__(self,age,hobby):
        self.age=age
        self.hobby=hobby
    def My_self(self):
        print(f"age is {self.age}, and hobby is {self.hobby}")
class Khan(Fardin):
    def __init__(self,age,hobby, hight,institute):
        self.hight=hight
        self.institute=institute
        super().__init__(age,hobby)
    def My_self(self):
        super().My_self()
        print(f'Your Hight is{self.hight},Your institute is {self.institute}')
class Azim(Fardin):
    def __init__(self,age,hobby,occap):
        self.occap=occap
        super(). __init__(age,hobby)
        
    def My_self(self):
         super().My_self()
         print(f"Occupaton\n{self.occap}")
object1=Khan(22,"Readin",5.5,"MRIST")
object2=Azim(18,"Reading","Str")

object1.My_self()
object2.My_self()

        