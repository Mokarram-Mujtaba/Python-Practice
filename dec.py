# def inner1(func):
#     def inner2():
#         print("Before function execution");
#         func()
#         print("After function execution")
#     return inner2
#
# @inner1
# def function_to_be_used():
#     print("This is inside the function")

# function_to_be_used()
# def mujtaba(func):
#     def hey():
#         a=5
#         b=6
#         sum=a+b
#         print(sum)
#         func()
#         print("Hey")
#     return hey
# @mujtaba
# def function_to_be_used():
#     print("This is inside the function")
# function_to_be_used()
# Python program to illustrate functions
# can be treated as objects
def shout(text):
	return text.upper()

print(shout('Hello'))

yell = shout

print(yell('Hello'))

# Python program to illustrate functions
# can be passed as arguments to other functions
# def shout(text):
# 	return text.upper()
#
# def whisper(text):
# 	return text.lower()
#
# def greet(func):
# 	# storing the function in a variable
# 	greeting = func("""Hi, I am created by a function passed as an argument.""")
# 	print (greeting)
#
# greet(shout)
# greet(whisper)
def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div = smart_div(div)
div(2,4)