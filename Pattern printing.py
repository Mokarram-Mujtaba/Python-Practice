for i in range(1,3):
    n=3

    for j in range(1,5):

        if j>=(n+1)-i and j<=(n-1)+i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print( )































































# n=int(input("How many rows you want to print"))
# k=bool(int(input("Chose 1 or 0")))
# if k==True:
#     for i in range(n):
#         # print(i)
#         for j in range(n):
#             if j<=i:
#                 print("*",end="")
#             else:
#                 print("",end="")
#         print()
# else:
#    for i in range(n):
#         for j in range(n):
#             if j>=i:
#                 print("*",end="")
#             else:
#                 print(end="")
#         print()












# x=int(input("ENter the number  of rows you want to print"))
#
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
#
# print("-------test---------------")
#
# for i in range(x,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
#
#
# for i in range(1,x+1):
#     for k in range(1,((x+1)-i)):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
# print("----------------")
#
# for i in range(x,0,-1):
#     for k in range(1,((x+1)-i)):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
# print("----------------")
#
# for i in range(x,0,-1):
#     for k in range(1,(x+1)-i):
#         print(" ",end=" ")
#     for j in range(1,(2*i-1)+1):
#         print("*",end=" ")
#     print("")
# print("----------------")
#
# for i in range(1,x+1):
#     for k in range(1,(x+1)-i):
#         print(" ",end=" ")
#     for j in range(1,(2*i-1)+1):
#         print("*",end=" ")
#     print("")
# print("----------------")
#
# for i in range(1,x+1):
#     for k in range(1,(x+1)-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")
# print("----------------")
# for i in range(x,0,-1):
#     for k in range(1,(x+1)-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print("")