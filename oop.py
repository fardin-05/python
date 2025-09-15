class A:
    def __init__(self,name,hight):
        self.name=name
        self.hight=hight
    def x(self):
        print(f"Name is:\n{self.name},\n age is:\n {self.hight}")
class B(A):
    def __init__(self,name,hight,age,hobby):
        self.age=age
        self.hobby=hobby
        super().__init__(name,hight)
    def x(self):
        super().x()
        print(f"age is \n {self.age},\n hobby is \n {self.hobby}")
class C(B):
    def __init__(self,name,hight,age,hobby,qualifications):
        self.qualification=qualifications
        super().__init__(name,hight,age,hobby)
    def x(self):
        super().x()
        print(f"Qualification is: \n {self.qualification}")
object=C("Fardin",5.5,18,"REading","Diploma student")
object2=B("Fardin",5.5, 22,"Programming")
object.x()
object2.x()
        

        
    