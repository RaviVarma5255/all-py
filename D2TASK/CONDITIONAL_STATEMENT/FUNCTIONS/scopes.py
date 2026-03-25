#SCOPE 
#scope refers to the region of a program where a variable is recognized or 
# accessible. It defines the visibility and lifetime of a variable.
#IN THIS WE HAVE 3 TYPES 1.LOCAL 2.GLOBAL 3.ENCLOSED SCOPE
#1.LOCAL SCOPE 
#Scope inside a function or method.
# Variables declared here are only accessible within that function.
# #EXAMPLE
# def multi():
#     x='varma'
#     print(x)
# multi() 
# ila istey radhu coz fun kinda ila rastey radhu , indentation lo rayali .:-

# def scope():
#     y=10
#     print(y)
# scope() #ilaa... we can call it as local , it is in inside the fun 
#what will happen we write outside the fun

# def local():
#     e=20
#     print(e)
# local() 
# print(e) #ila istey e not defind anii vastadi becoz manamu outside of the local rasamu kabbati.. oka vella niku kavali anukutey 

# def local():
#     global e
#     e=20
#     # print(e)
# local()
# print(e) #ila istey print avutadi coz global modifiers.. ikkada fun call ivakapotey print avadhu op 2tuu 20 print avutai
#name 'e' is not defined ila vastadi..

#2.GLOBAL SCOPE
# b='hello'
# def hi():
#    print(b)
# hi() 

# v='ravi varma'
# def name():
#    global y
#    y='varma'
   
   #ila istey 1st varma print ayyi next ravi varma print avutadi ala kakunda 
   #1st rv print avali antey  indentation tiseyi rayi
# name() 
# print(y)


# a=10
# def know(c,b):
#    return c+b
# result=know(5,7)
# print(result)
# print(a) a fun out side untadi kabbati ekkada ichina kuda print avutadi...

#3.ENCLOSED SCOPE 
# def enclosed():
#    def name():
#      e=23
#      print(e)
#    name()
# enclosed() #ikkada 2 funs vadamu enclosed & name , indulo 2nd fun lo e ichamu aa print inside name lo istey print avutadi
#lekkapote error vastadi

# def fuc1():
#    y=20
#    def fuc2():
#       l='ravi'
#       print(l)
#    fuc2()
#    print(y)
# fuc1()

#NON LOCAL 
# def outer():
#    y=30
#    def inner():
#       nonlocal y
#       y=20
#       print(y)
#    inner()
#    print(y)
# outer() #With nonlocal, the inner and outer function share the same variable — and changes made inside are reflected outside.



# local scope
# antey inside d scope chudam 
# def q():
#     global x
#     x='varma'
#     # print(x)
# q()
# print(x)
# adey indulo ney manamu global x ani istey bhayatha ichi vastadi

# 2 global scope
#  antey global mottam antey daniki apply avutadi
# manamu bhayatha ivachu lopala ivachu
# v='hi'
# def b():
#     global x
#     x='varma'
#     print(v)
# b()
# print(x)


# def a():
#     global v
#     v=20
#     print(v)
# a()
# print(v)


# y=25
# def a():
#     global v
#     print(y)
#     v=20
#    #  print(v)
# def b():
#     print(y)

# a()
# b()
# print(v)

# encolsed scope 

# def o():
#     v=10

#     def i():
#       print(v)

#     i()

# o()

# sunny number 
# ichina number ki +1 cheyali 

a=int(input('enter a number :'))
for i in [a]:
    m=(i+1) ** 0.5
    if m == int(m):
        print('sunny')
    else:
        print('not sunny')
