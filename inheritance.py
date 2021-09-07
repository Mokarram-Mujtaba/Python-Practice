# class V2d:
#
#     def __init__(self, i, j):
#         self.icap = i
#
#         self.jcap = j
#
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"
#
# class V3d(V2d):
#
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k
#
#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
#
# v2 = V2d(1, 5)
# v3 = V3d(1, 5, 7)
# print(v2)
# print(v3)


# class Employee():
#     salary=200
#     increment=1.5
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary*self.increment
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,sai):
#         self.increment=sai/self.salary
# e=Employee()
# print(e.salaryAfterIncrement)
# class Employee():
#     salry=500
#     increment=2
#     @property
#     def salaryAfterIncrement(self):
#         return self.salry*self.increment
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,inc):
#         self.increment=inc/self.salry
# e=Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement=500
# print(e.increment)

# class Complex:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, other):
#         return Complex(self.real+other.real , self.imaginary + other.imaginary)
#     def __mul__(self, other):
#         mulreal=self.real+other.real - self.imaginary + other.imaginary
#         mulimaginary = self.real + other.real + self.imaginary + other.imaginary
#         return Complex(mulreal,mulimaginary)
#     def __str__(self):
#         if self.imaginary<0:
#             return f"{self.real}-{-self.imaginary}i"
#         else:
#             return f"{self.real}+{self.imaginary}i"
# c1=Complex(1,-2)
# c2=Complex(1,-3)
# print(c1+c2)
# print(c1*c2)
