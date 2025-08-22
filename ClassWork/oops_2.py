class Driver:
    def dispaly(self,name,gender,vehno,vehtype):
        self.name=name
        self.gender=gender
        self.vehno=vehno
        self.vehtype=vehtype
        print("Driver Details")
        print(self.name)
        print(self.gender)
        print(self.vehno)
        print(self.vehtype)
class FareCal:
    def display(self):
        print("2_Wheelers")
        print("3_wheelers")
        print("4_Wheelers")
obj=FareCal()
obj.display()
'''
2_Wheelers
3_wheelers
4_Wheelers
'''
#Note---->If we have the same name for inheritance concept then super() is used access from the parent class
class Driver:
    def dispaly(self,name,gender,vehno,vehtype):
        self.name=name
        self.gender=gender
        self.vehno=vehno
        self.vehtype=vehtype
        print("Driver Details")
        print(self.name)
        print(self.gender)
        print(self.vehno)
        print(self.vehtype)
'''
class FareCal:
    def display(self,name,gender,vehno,vehtype):
        super().display(name,gender,vehno,vehtype)
        print("2_Wheelers")
        print("3_wheelers")
        print("4_Wheelers")
obj=FareCal()
obj.display('xyz','xud','dbsu','hed')

'''
class A:
    def print_(self):
        print("This is parent class: A")
class B:
    def print_(self):
        print("This is child class: B")
class C(A,B):
    def print_(self):
        A.print_(self)
        B.print_(self)
        print("This is grand child class: C")
c=C()
c.print_()
