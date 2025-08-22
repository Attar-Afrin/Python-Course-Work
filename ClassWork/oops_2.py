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
'''
This is parent class: A
This is child class: B
This is grand child class: C
'''
#example of inheritance
class Phone:
    def __init__(self,user):
        self.user=user
        print(f"Hello {self.user} Welcome, enjoy the features Like")
        print("Call")
        print("SMS")
        print("Games")
        print("Alarm")
        print("FM Radio")
class Phone_V1(Phone):
    def __init__(self,user):
        self.user=user
        super().__init__(user)
        print("Camera")
        print("Bluetooth")
        print("4G Internet")
        print("Finger Print")
class Phone_V2(Phone_V1):
    def __init__(self,user):
        self.user=user
        super().__init__(user)
        print("5G Internet")
        print("Scanner")
        print("Face_id")
class Phone_V3():
    def __init__(self,user):
        self.user=user
        print("This is trail Features")
        print("Thiz is the Trail Features")
        print("AI_Integration")
        print("Updated_system")
        print("Maps")
class Phone_V4(Phone_V3,Phone_V2):
    def __init__(self,user):
        self.user=user
        Phone_V3.__init__(self,user)
        Phone_V2.__init__(self,user)

        print("Thiz is the Trail Features")
        print("AI_Integration")
        print("Updated_system")
afreen=Phone('afreen')
ramya=Phone_V1('ramya')
revathi=Phone_V2('revathi')
keerthan=Phone_V3("keerthana")
nihitha=Phone_V4("nihitha")
'''
This is parent class: A
This is child class: B
This is grand child class: C
Hello afreen Welcome, enjoy the features Like
Call
SMS
Games
Alarm
FM Radio
Hello ramya Welcome, enjoy the features Like
Call
SMS
Games
Alarm
FM Radio
Camera
Bluetooth
4G Internet
Finger Print
Hello revathi Welcome, enjoy the features Like
Call
SMS
Games
Alarm
FM Radio
Camera
Bluetooth
4G Internet
Finger Print
5G Internet
Scanner
Face_id
This is trail Features
Thiz is the Trail Features
AI_Integration
Updated_system
Maps
This is trail Features
Thiz is the Trail Features
AI_Integration
Updated_system
Maps
Hello nihitha Welcome, enjoy the features Like
Call
SMS
Games
Alarm
FM Radio
Camera
Bluetooth
4G Internet
Finger Print
5G Internet
Scanner
Face_id
Thiz is the Trail Features
AI_Integration
Updated_system
'''  
    
     
    

