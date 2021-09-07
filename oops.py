'''
Employee infomation
Practice set

Question:-1
'''
# class Programmer:
#     company="Microsoft"
#     def __init__(self,name, projec,employeid,post):
#         self.name=name
#         self.projec=projec
#         self.id=employeid
#         self.post=post
#     def get_detais(self):
#         print(f"name {self.name } working on {self.projec}\nemployee id {self.id}\nand he is {self.post} Developer  ")
# mujtaba=Programmer("MM","GIT",1205,"Senior")
# mujtaba.get_detais()

'''
Practice 2
'''
# class Calculator:
#     def __init__(self,number):
#         self.number=number
#     def sqaare(self):
#         print(f'Square of {self.number} is {self.number**2}')
#     def cube(self):
#         print(f"Cube of {self.number} is {self.number**3}")
#     def squareroot(self):
#         print(f"sqaure root of {self.number} is {self.number**0.5}")
# i=int(input("Enter the number you want to calculate"))
# calculation=Calculator(i)
# j=int(input("what do you want \n press 1 for sqaure \n press 2 for cube \n press 3 for square root \n"))
# if j==1:
#     calculation.sqaare()
# elif j==2:
#     calculation.cube()
# elif j==3:
#     calculation.squareroot()
# else:
#     print("Enter a valid option")
'''
________________________________________________________________________
Practice 3
'''
# class a:
#     b="RAJA"
#
#     @staticmethod
#     def greet():
#         print("You are Under static method")
#
# object=a()
# object.b="mujju"
# object.greet()
# print(object.b)
# print(a.b)

# changing the object instance attribute will not affect on class attribute it will create only a another instance
'''
**********************
Practice 5
'''
class Train():
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    def booktkt(self):
        if self.seats>=0:
            print(f"Booking successfull in \n{self.name} Fair is {self.fare} \nYour seat number is {self.seats} ")
            self.seats=self.seats-1
            # c=self.seats
        else:
            print("Seat full please check for another train ")

    # def canceltlkt(self):
    #     if self.seats>seats:
    #         print("No previous ticket booked")
    #     else:
    #         print("Canclledd")


c=400
stabdi=Train("Stabadi Express train number 1555",c,600)
# stabdi.booktkt()
# stabdi.canceltlkt()
# stabdi.canceltlkt()
# stabdi.booktkt()
# stabdi.booktkt()
# stabdi.booktkt()
# stabdi.booktkt()
# stabdi.booktkt()
# stabdi.booktkt()