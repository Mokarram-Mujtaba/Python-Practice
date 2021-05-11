x=int(input("ENter the number  of rows you want to print"))

for i in range(1,x+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")

print("-------test---------------")

for i in range(x,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")


for i in range(1,x+1):
    for k in range(1,((x+1)-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
print("----------------")

for i in range(x,0,-1):
    for k in range(1,((x+1)-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
print("----------------")

for i in range(x,0,-1):
    for k in range(1,(x+1)-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
        print("*",end=" ")
    print("")
print("----------------")

for i in range(1,x+1):
    for k in range(1,(x+1)-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
        print("*",end=" ")
    print("")
print("----------------")

for i in range(1,x+1):
    for k in range(1,(x+1)-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
print("----------------")
for i in range(x,0,-1):
    for k in range(1,(x+1)-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
