#Single level Inheritance






#Multi Level
class A:
    def printa(self):
        print("This is the parent class_A")
class B(A):
    def printb(self):
       print("This is the chilld Class:B->A")
class C(B):
    def printc(self):
       print("This is the child class:C->B->A")

c=C()
c.printa()
c.printb()
c.printc()
'''
This is the parent class_A
This is the chilld Class:B->A
This is the child class:C->B->A
'''
#Multiple Inheritence
class A:
    def printa(self):
        print("This is the parent class_A")
class B(A):
    def printb(self):
       print("This is the chilld Class:B->A")
class C(B):
    def printc(self):
       print("This is the child class:C->B->A")
       print("Hii")
class D(C,B,A):
    def printd(self):
        print("This is class:D (A--B--C)--->D")
        print("Multiple Parents single Child is called multiple inheritance")
d=D()
d.printd()
d.printa()
d.printb()
d.printc()

#Hierarcial Inheritance

print("This is the Example for the oops Concept")
class Person:
    def login(self,name,ph_no,gender):
        self.name=name
        self.ph_no=ph_no
        self.gender=gender
class Driver(Person):
    def driverDetails(self,vehno,photo,vetype):
        self.vehno=vehno
        self.photo=photo
        self.vetype=vetype
        print(f"\n Hello {self.name}\n Your Driver account is Succesfully created")
class DriverRides:
    def driver_rides(self,exp,totalrides):
        self.exp=exp
        self.totalrides=totalrides
        print(f"\n Hello {self.name}\n Your ride details are updated")
class wheels_2:
    def price_2W(self):
        self.fare=30
        return self.fare
    


class User(Person):
    def userdetails(self,drop,pickup):
        self.pickup=pickup
        self.drop=drop
        print(f"\n Hello {self.name}\n You Booked Ride Succesfully")
afreen=User()
print(afreen.login)
