'''
code that might through errors
'''

# while(True):
#     print("Press Q for quite")
#     a=input("Enter the number")
#     if a=="Q":
#         break
#     try:
#         print("Trying...")
#         a=int(a)
#         if a>6:
#             print("You have entered a larger number")
#     except Exception as e:
#         print(e)
# print("Thank you for playing this game")

'''
handling expceptotions using except exception simple using try and and Except
'''

# try:
#     a=int(input("Enter the number n"))
#     c=1/a
#     print(c)
# except Exception as e:
#     print('exception occured')
#     print(e)
# print("Thanks you very much")

'''
exception for particular errors
'''
try:
    a=int(input("Enter the number"))
    b=1/a
    print(b)
except ValueError as e:
    print("Value eroor",e)
except ZeroDivisionError as e:
    print("ZeroDivisionEroor",e)
print("DONE")







# def inceremnet(num):
#     try:
#         return int(num)+1
#     except:
#         raise ValueError("This is error")
# a=inceremnet("5f4")
# print(a)