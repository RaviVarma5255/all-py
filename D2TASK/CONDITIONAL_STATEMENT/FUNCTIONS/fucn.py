#What is a Function?
# A function is a reusable block of code/statements that performs a specific task. It helps organize code and avoid repetition.
# The idea is to put some commonly or repeatedly done tasks together and make a 
# function so that instead of writing some code again and again for different inputs,
#  we can do the function calls to reuse the code contained in it over and over again.
#def is keyword to define a function..

#return – Gives a value back to the caller
# Purpose: Used to send a value out of a function.

# Effect: Ends the function and hands back a result.

# Usage: The returned value can be stored in a variable or used in other expressions.

#print – Displays output to the screen
# Purpose: Used to show output to the console (for humans to read).

# Effect: Does not return a value from a function.

# Usage: For debugging or user messages.

 #1.Calling a Function
# def fun_name():
#     print('hello')
# fun_name() #here i call the function if we cont call the fun then it will not print
#we should called multiples times and any where we want...

#example 
# def ravi(a,b):
#     return a+b
#     # r=a+b
#     # print(r)
# print(ravi(4,6))
# print(ravi(2,5))
# ravi(1,2)
# ravi(1,8) 
# ravi(100,500)
#The function ravi does return a value (the sum), but you are not doing anything with that value.
# # You're not printing it, storing it in a variable, or using it in any way. if want that calling fun then put print(ravi(1,2))
#or store that values in variables..

#Return Values  example
#A function can return data using return:
# def sub(c,d):
#     return c-d
# subs=sub(7,3)
# print(subs)

# without return 
# def sub(c,d):
#     print('bollo')
# subs=sub(7,3) ikkada manamu emi c and d ki values assign cheyaliey 
# print(subs) #ila return ivvakapotey none and print lo unadi print avutadi..


#2.FUNCTION WITH PARAMETERS..

#In Python, functions with parameters allow you to pass information (called arguments) 
# into a function so it can perform actions using that data.

#<<with out return >>
# def fuc_py(name): >> it iis called parameter
#     print(name,'hii')
# fuc_py('ravi') >> this is called argument
# fuc_py('varma') >>this is called argument

def a_b(name): 
    # >> it iis called parameter
    print('ravi',name)
    return ('i am from kakinada')
a_b('varma')
a_b('luli')
# ..>> this is called argument

# def greet(name):
#     print(' hi this is',name)
#     return 'i am completed my btech'
# v=greet('ravi varma')
# print(f'{v} in kiet+') 

# def name(a,b):
#     print(a[0],b[0])
# name('ravi','varma') op:-rv

#3.Default Parameter Value 
#If a parameter has a default value, it becomes optional

#without return..
# def greet(name="Guest"):
#     print(f"Hello, {name}!")
# greet('ravi')         # Output: Hello, Guest!
# greet("Sam")    # Output: Hello, Sam!

# WITH RETURN
# def billing(price,gst=0.18):# the default will be not change ,& u can see here the price value will be taking coz we given the default value
#     total_price= price+gst*price
#     return total_price
# print(billing(145))
# print(billing(128))
# print(billing(250,0.28))..

#4.Number of Parameters
#Functions must be called with the correct number of arguments:
#example:-
# def add(a,b,c):
#     print(a+b+c)
# add(1,3,) #add() missing 1 required positional argument: 'c'

# def add(x,y,z): 
#   return x+y+z
# v=add(10,20,30)
# print(v)
# print(add(1,2,3))
# print(add(2,4,5))

#5. ARBITARY ARGUMENTS 
#IT WILL WIRTTEN AS (*)
#If you're not sure how many arguments will be passed, use *args.
#EXAMPLE
# def amen(*a):
#     print('i want',a)
# amen('books','pens','ideeas','etc') #like this with *a this we print some arguments..

#6. postion argument
# def devara_movie(hero,heroin,villan):
#     print(hero,heroin,villan)
# devara_movie('ntr','salif','janvi') ila edo order lo ochamu 
#to overcome this we use key arguments..
 

#6.KEY ARGUMENTS
# You can also pass values with keys, known as keyword arguments
# def  devara_movie(hero,heroin,villan):
#     print(f'hero:{hero} ,heroin:{heroin},villan:{villan}')
# devara_movie(heroin='jannvi',hero='NTR',villan='ali khan') #op;-hero:NTR ,heroin:jannvi,villan:ali khan

#7. LAMBDA FUCNTIONS
#   IT IS USED TO PERFORM SIMPLEST TASK WITH VERY SHORT FORM OF THE FUN DEFINITION
# IT IS A ANONYMOUS FUNCTION , A FUN WITHOUT HAVE NAME IS CALLED ANONYMOUS FUN..
# EXAMPLE
#1.WITHOUT PARAMETERS
# a=lambda: 'hii'
# print(a())
#a → refers to the function itself
# a() → calls the function and returns 'hii'

#2.WITH PARAMETERS
# b=lambda a,h:a+h
# print(b('ravi','varma'))

# c=lambda w,e,r:w+e-r
# print(c(5+2-1,3,1)) #:- ikkaada chusukunatu ayitey w,e,r icahmu & vatiki aruguments w ki 5+2-1 
#edi antha oka w arugument kinada tesukuntadi as (w),and migggatavi 3&1 nii e emo e & r emo 1...
# v=lambda *abc: sum(abc)
# print(v(1,2,4,5,6,23,2,342,12)) 

# def ravi():
#     x=45
#     def varma():
#         x=20
#         print(x)
#     print(x)
#     def chandra():
#         print(x)
#         chandra()
#     varma()
# ravi()


# def a(b,c):
#     return b+c
# print(a(1,0))
# print(a(4,7))


# def varma(a,b,c):
#     return a+b+c
#     t=a+b+c
#     print(t)
# varma(10,20,30)
# varma(20,5,5)
# print(varma(10,20,10))
# print(varma(10,20,10))



def square(n):
    return n * n # returning the square, not printing

# We can reuse the returned value
x = square(5)
print(x)           # 25

y = square(x)
print(y)           # 625















