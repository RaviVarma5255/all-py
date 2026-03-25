# What is OOP?
# OOP stands for Object-Oriented Programming.
# Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

# Advantages of OOP :-
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code
# Tip: The DRY principle means you should avoid writing the same code more than once. Move repeated code into functions or classes and reuse it.

# What are Classes and Objects?
# Classes and objects are the two core concepts in object-oriented programming.
# A class defines what an object should look like, and an object is created based on that class. For example:
# Class	Objects
# Fruit	Apple, Banana, Mango
# Car  	Volvo, Audi, Toyota

# Python Classes/Objects :-
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

#<<<<<<EXAMPLES OF CLASS AND OBJ>>>>>>..
# class ravi:
#     name='varma'
#     age=22
# ravi()
# print(ravi)
# p=ravi()
# print(p)

# class Ravi:
#     d = 20

#     def a(self):  # 'self' refers to the object calling the method
#         name = 'ravi'
#         age = 22
#         print(name, age)

# ob = Ravi()     # Create an object 'ob' from class Ravi
# ob.a()          # Call method 'a' using the object 'ob'

# class K:
#     d='ravi'
#     v=20
#     def a(slef):
#         a=10
#         b=20
#         print(a+b)

# print(K.d,K.v)
# ob=K()
# ob=ob.a()
# print(K.d,K.v)

# even or odd

# class Ab:
#     def Bb(self,Bb):
#          if Bb%2==0:
#            print('it is a even num')
#          else:
#              print('it is odd num')
# ob=Ab()
# ob.Bb(2)
# ob.Bb(5)

#The __init__() Method
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() method.

# class Hi:
#     def __init__(self,name):
#         self.name=name
#         # print(f' my name is {name}')

# obj = Hi('ravi')
# print(obj.name)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name,p1.age)
# print(p1.age)

#inheritance in this we have 5 types
# 1 single level 2 multiple level 3 multi level 4 hyrarical 5 hybrid 

# class Parent:
#     def __init__(self,pv): parameters
#         self.Va=pv instance variables
# class Child(Parent):
#     def __init__(self, pv,cv):
#         super().__init__(pv)
#         self.va=cv
#         print(f'parent value is {self.Va}  andvalue is {self.va}')
# ob=Child(11,212) instance object


# class ravi:
#     def a(self,b):
#         print(b)
# c=ravi()
# c.a('varma')

#class ravi:
#     def a(self,b):
#         self.b=b
#         print(self.b)
# c=ravi()
# c.a('varma')

# class ravi:
# You're defining a class named ravi. ✅
# def a(self, b):
# You're creating a method called a inside the class.
# self refers to the object (instance) that will call the method.
# b is a parameter — you’ll pass a value into it when calling the method.
# print(b)
# The method prints the value of b.
# c = ravi()
# This creates an object (or instance) of the class ravi.
# So yes: ✅ c is the instance object of the class.
# c.a('varma')
# You're calling method a on object c.
# 'varma' is passed as the argument to b.
# Internally, Python does: ravi.a(c, 'varma')
# self = c, and b = 'varma'

# class ravi:
#     def a(self,b,w,r):
#         self.b=b
#         print(self.b,w,r)
# v=ravi()
# v.a('varma','w',3132)

# class repu:
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
# r=repu('k')

# class repu:
#     def __init__(self, a):
#         self.a = a

#     def update_a(self, value):
#         self.a = value
#         print(f'Updated a: {self.a}')

# r = repu('initial')
# r.update_a('new')    # ✅ now you're calling a method

# class ewwy:
#     def r(self,name):
#          self.name = name
#          print(self.name) 
     
#     def ravi(self,p,s):
#         self.p=p
#         self.s=s
#         print(self.p)
#         print(self.s)

#     def varma(self,h,p):
#         self.h=h
#         self.p=p
#         print(self.h,self.p)
# i=ewwy()
# i.varma('hello',44)
# i.ravi('ravi',89)


# class ewwy:
#     def r(self, name):
#         self.name = name
#         print(self.name)
     
#     def ravi(self, p, s):
#         self.p = p
#         self.s = s
#         print(self.p, self.s)  # ✅ fixed line

#     def varma(self, h):
#         self.h = h
#         print(self.h)

# i = ewwy()
# i.varma('hello')         # Output: hello
# i.ravi('ravi', 21)       # Output: ravi 21

#inheritance it means :- creating one new class from already created class
#in this we have 5 types
#1 single level 2 multiple 3 multi 4 hierarchical 5 hybrid
#1 sigle it as one parent and one child

#examples



class Parent:

    def __init__(name):
        name.pname=name
        print('hi')

class Child(Parent):

    def Ntr(self):
        print('hello')
ch=Child()
ch.Ntr()



# class Parent():
#     def Pmethod(a):
#         print('i am from parent class')
#     def Pmethod2(a): #nuv u.Pmethod anni ichamu antey direct kinda undai print avutadi
#         print('i am from method 2')

# class Child(Parent):
#     def Cmethod(a):
#         super().Pmethod2() # adey Cmethod istey first super. unna di print avutadi and kida i mean cmethod lo print avvutadi
#         super().Pmethod()  # for accessing for parent class
#         print('i am from child class')

# u=Child()
# # u.Pmethod()
# # u.Pmethod2() ila pilla kunda super istey access avutadi
# u.Cmethod()


# class Method1:
#     def ntr(self):
#         self.n_worth=100
#         print({self.n_worth},'cr is the ntr worth')

# class Method2(Method1):
#     def BargavRam(self):
#         self.b_worth=50
#         print({self.b_worth},'cr is the bargavram worth')

#     def total_worth(self):
#         self.ntr() #ikkada super vadakapoyina direct gaa self . ichi niku kavalisina method name ivachu
#         self.BargavRam()
#         total_worth=self.n_worth+self.b_worth
#         print({total_worth},'cr is the abayaram worth')

# ar=Method2()
# # ar.BargavRam()
# ar.total_worth()


# #firat nuchi nerchukuntam
# 1. What is a class? Write syntax and one example.
# A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects (instances) will have.
# In Python, when you define a method inside a class, you must use self as the first parameter for instance methods.


# Syntax:
# class ClassName:
#     def __init__(self): ikadda self annadi object kii instance
#         # attributes
#         pass

#     def method(self):
#         # method logic
#         pass

# class L:
#     def hi(self,b):
#         self.name=100
#         self.b=b
# x=L()
# x.hi('hello') #indulo unavi avutayi
# print(x.name)
# print(x.b)

# class Ravi:
#     def varma(self):
#         self.a=100
# s=Ravi()
# s.varma()
# print(s.a)

# class varma:
#     def ravi(self):
#         self.name='name'
# c=varma()
# c.ravi()
# print(c.name)
# <<<<<<<<<<<<<<<<<<USING INIT >>>>>>>>>>>>>>>>>>>>>
# class Ravi: 
#     def __init__(self,k):
#         self.varma = k
# z = Ravi(k='l') #init method use chestey ravi anna object lo ney ivlai "l anni" ivachu or k='l anni ivachu
# print(z.varma)


#<<<<<<<<<OBJECT>>>>>>>>>>>>>>
#obje is nothing but instance of a class   it is created by a class and it will represent a attributes(data) and method(function)
#like .
#what does obj contains
#object contains attributes and methods
#attributes do store the specific of the object

# class i:
#     a='helllo' #iddi class ki attributes
#     def f(self):
#         self.hel=1000
# c=i() #here c is the obj of class i
# c.f() #and i access the method f in 
# print(c.a)
# print(c.hel) #and i print the attribute of class in object
        
# class Cars:
#     def __init__(self,company):
#         self.a=company
#     def Drive(self):
#         print('volvo')
#     def Color(self,s):
#         self.b=s

# c=Cars('tata')
# print(c.a)
# c.Drive()
# c.Color('red')
# print(c.b) #kachitanga print cheyali

# class classname:
#     name=10
# class child(classname):
#     name=20
# v=child()
# print(v.name)

#<<<<<<<<<<<<<INHERITANCE>>>>>>>>>>>>>>>
#IN THIS WE HAVE 5 TYPES 
#1 SINGLE INHERITANCE
#2 MULTIPLE INHERITANCE
#3 MULTI INHERITANCE
#4 Hierarchial
#5 hybrid

#1 single inheritance 

#syntax :-
#class Parent:
#code (att/methods)
#class Child(Parent):
#code that can be use parent features

#example

# class Parent:
#     def pclass(self):
#         self.name='raju'
# class Child(Parent):
#     def cclass(self):
#         self.a='varma'
# v=Child()
# v.pclass()
# v.cclass()
# print(v.a,'is the child of',v.name)

#<<<<chat gpt ques >>>>>>

# class Vehicle:
#     def show_wheels(self,a):
#         self.wheels=a
#         print('Number of wheels:',a)
# class Car(Vehicle):
#     def show_brand(self,b):
#         self.b=b
#         print('car brand:',b)
# m=Car()
# m.show_brand('toyota')
# m.show_wheels(4)

# using init

# class Vechile:
#     def __init__(self,a):
#         self.a=a

#     def show_wheels(self):
#         print('Number of wheels:',self.a)

# class Car(Vechile):
#     def __init__(self,a,brand):
#         super().__init__(a)
#         self.c=brand

#     def show_brand(self):
#         print('Car brand:',self.c)

# m=Car(4,'toyota')
# m.show_wheels()
# m.show_brand()

# class Dog:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# p=Dog('lucy','lab')
# print('dog name is :',p.a)
# print('dog breed is :',p.b)
        
#without super function

# class Animal:
#     def __init__(self,a):
#         self.a=a
#     def sound(self):
#         print(self.a,'are angry')
# class Dog(Animal):
#     def breed(self):
#         print(self.a,'breed is lab')
# c=Dog('lucy')
# c.sound()
# c.breed()


#<<<<<<<<<< USING SUPER WITH INIT >>>>>>>>>>>>>>>>>>>>>>>>
# class ParentActor:
#     def __init__(self,pname,pworth):
#         self.a=pname
#         self.b=pworth
#         print(self.a,'is the parent')
    
#     def Passests(self):
#         print(self.a,'assests are',self.b,'cr')

# class Childactor(ParentActor):
#     def __init__(self, pname, pworth,cname):
#         super().__init__(pname, pworth) #ikkada self .pname and kinda self.pworth ivakunda direct ga super lo rendu use cheysamu...
#         self.c=cname
#         print(self.c,'is come referance of',self.a)
    
#     def Cassests(self,cworth):
#         self.d=cworth
#         print(self.c,'is having worth of ',self.d)

#     def Totalworth(self):
#         print('total worth is',self.b + self.d)

# z=Childactor('hari',100,'ntr')
# z.Passests()
# z.Cassests(90)
# z.Totalworth()
    
#without init we use super like this
# class Animal:
#     def sound(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         super().sound()  # Call parent version first
#         print("Dog barks")

# d = Dog()
# d.sound()
# d.speak()

# class Prent:
#     def Pmethod(self):
#         print('i am from parent class')
# class Child(Prent):
#     def Cmethod(self):
#         print('i am from chlid class')

# v=Child()
# v.Pmethod()
# v.Cmethod()


# <<<<<<<<<<MULTIPLE INHERITANCE >>>>>>>>>>>>>>>>>>>>>>
# class Parent1:
#     def Pmethod1(self):
#         print('i am from parent1')
# class Parent2:
#     def Pmethod2(self):
#         print('i am from parent2')
# class Child(Parent1,Parent2):
#     def cmethod(self):
#         print('i am from child')
# v=Child()
# v.Pmethod1()
# v.Pmethod2()
# v.cmethod()

# class Human:
#     def eat(self):
#         print('i can eat')
#     def work(self):
#         print('i can work')
# class Male:
#     def flirt(self):
#         print('i can flirt')
#     def work(self):
#         print('i can do work')
# class Boy(Human , Male):
#      def work(self):
#          print('i can do wrok 2')
# o=Boy()
# o.work()
# Male.work(o)
# # Human.work(o)
# # ila access cheysukovachu class name and method name(obj)
#Male.work(o.mro())

# class Vechle:
#     def start(self,start1):
#         self.a=start1 #self.a is a variable to store the variables
#     def stop(self,stop1):
#         self.stop1=stop1 
# class Car:
#     def start(self,start2):
#         self.start2=start2
#     def stop(self,stop2):
#         self.stop2=stop2
# class Road(Vechle,Car):
#     def start(self,start1,stop1, start2,stop2,start3):
#         self.start3=start3
#         Vechle.start(self,start1)
#         Vechle.stop(self,start1)
#         Car.start(self,start2)
#         Car.stop(self,stop2)
#         print(start1,'start the engine')
#         print(stop1,'after completed the drive stop the engie')
#         print(start2,'start the bike')
#         print(stop2,'stop the bike')
#         print(start3,'start the coding')

# v=Road()
# v.start('ravi car','ravi','varma ','varma','python code')

# class Parent1:
#     def __init__(self,pname,phone_pnumber):
#         self.pname=pname
#         self.phone_number=phone_pnumber
# class Parent2:
#     def __init__(self,mname,phone_mnumber):
#         self.mname=mname
#         self.phone_mnumber=phone_mnumber
# class Child(Parent1,Parent2):
#     def __init__(self, pname, phone_pnumber,mname,phone_mnumber,cname,cnumber):
#         Parent1.__init__(self,pname, phone_pnumber)
#         Parent2.__init__(self,mname,phone_mnumber)
#         self.cname=cname
#         self.cnumber=cnumber

# rs=Child(pname='Raju',phone_pnumber=9391443569,mname='padmavathi',phone_mnumber=9676926169,cname='ravi',cnumber=7989740659)
# print(f'{rs.pname} is the father of {rs.cname}')
# print(f'{rs.mname} is the mother of {rs.cname}')
# print(f'{rs.cname} father phone number is {rs.phone_number}')
# print(f'{rs.cname} mother phone number is {rs.phone_mnumber}')
# print(f'{rs.cname} phone number is {rs.cnumber}')

#<<<<<<< MULTI INHERITANCE >>>>>>>>>>>>
#Multi-level inheritance means a class inherits from a class that has already inherited from another class.
# class Grandfather:
#     def house(self):
#         print("I am from grand father")

# class Father(Grandfather):
#     def car(self):
#         print("I am from father")

# class Son(Father):
#     def bike(self):
#         print("I am from son")

# s = Son()
# s.bike()
# s.house()
# s.bike()
# s.car()

# class Gp:
#     def grand(self,name,age):
#         self.name=name
#         self.age=age
#         # print(f'{self.name} is the father of {self.fname}')
#         # print(f'{self.name} has {self.age} years old')
# class F(Gp):
#     def Father(self,name,age):
#         self.name=name
#         self.age=age
# class C(F):
#     def son(self,name,age):
#         self.name=name
#         self.age=age

# gf=Gp()
# gf.grand('divakar raju',91)

# s=C()
# s.son('ravi varma',22)

# f=F()
# f.Father('rama krishna raju',61)

# print(gf.name)
# print(f.name)
# print(s.name)
#ila parthi class ki own obj tisukunamu anndhu aa object.parameter ni use chyali

# class P1:
#     def Grand1(self):
#         print('i am from grand father class')

# class P2(P1):
#     def Fatther1(self):
#         print('i am from father class')

# class P3(P2):
#     def Child(self):
#         print('i am from child class')

# o=P3()
# o.Grand1()
# o.Fatther1()
# o.Child()

# class G1:
#     def grand(self):
#         print('devakar raju')  
#     def grand_wife(self):
#         print('subbayama')
# class F1(G1):
#     def father(self):
#         print('rama krishna raju')
#     def father_wife(sefl):
#        print('padmavathi')
# class C1(F1):
#     def child(self):
#         print('ravi varma')
# class C2(F1):
#     def child2(self):
#         print('sravani')
# family=C2()
# family.grand()
# family.grand_wife()
# family.father()
# family.father_wife()
# C1.child(family) #ikkada iddi derived avely andukey , c2 lo f1 undi c lo kuda vundi but latrst ga vachinadey kadha tisukuntadi soo ala f1 class ki 
# #veltadi akkada aa methods ni class cheystey print cheystadi and andulo ney g1 undi kabbatti addi access cheysukovachu
# family.child2()

# class grand:
#     def __init__(self,name,village):
#         self.name=name
#         self.village=village
    
#     def grand(self):
#         print(f'{self.name} is from {self.village}')
        

# class father(grand):
#     def __init__(self, name, village,fname,fvillage):
#         super().__init__(name, village)
#         self.fname=fname
#         self.fvillage=fvillage
    
#     def father(self):
#         print(f'{self.fname} is from {self.fvillage}')
#         print(f'{self.name} is the father of {self.fname}')
#         print(f'{self.fname} is the son of {self.name}')

# class child(father):
#     def __init__(self, name, village, fname, fvillage,cname,cvillage):
#         super().__init__(name, village, fname, fvillage)
#         self.cname=cname
#         self.cvillage=cvillage

#     def child(self):
#         print(f'{self.cname} is from {self.cvillage}')
#         print(f'{self.fname} is the father of {self.cname}')
#         print(f'{self.name} is the grandfather of {self.cname}')

# ml=child('devakar raju','namavani palem','rama krishna raju','namavanipalem','ravi varma','namavaniplaem')
# ml.grand()
# ml.father()
# ml.child() #adi nuv main class lo derived class lo unna parameters access cheyali antey daniki if use chysi andulo bluit in function vadali 
#Yes, exactly! hasattr is a built-in Python function (you could call it a “method” in casual terms,
#  but technically it’s a function) that checks whether an object has a particular attribute.

#ABSTRACT METHOD 

# for i in range(65,91):
#     if i == ord('D'):
#        print(chr(i))
#        break

# Class = Blueprint
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def drive(self):
#         print(f"{self.color} {self.brand} is driving...")

# # Objects = Real cars created from the blueprint
# car1 = Car("Tesla", "Red")
# car2 = Car("BMW", "Black")

# car1.drive()   # Red Tesla is driving...
# car2.drive()   # Black BMW is driving...


# class room:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def lulu(self):
#         print(f'{self.a} is the brand of {self.b}')

# a=room('hello','varma')
# a.lulu()

# a=int(input('enter the number :'))
# b=a
# sum=0

# for i in str(a):
#     sum+=int(i)**3

# if sum==b:
#     print('it is a arm strong number')
# else:
#     print('it is a not a armstrong number')

# a=153
# s=0
# for i in str(a):
#     s+=int(i)**3
# if s==a:
#     print('nh')
# else:
#     print('n')
     


    
