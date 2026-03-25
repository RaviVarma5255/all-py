# syntax and semantic

# syntax : the set of rules that define how you must write the code so that d python will understand iter

# print('hello world !') is the correct syntax
# print ('heloo it is not correct syntax
# next semantics = it as a meaning of ur code
# x= 10 / 2 divided 10 by 2 is right Syntax

# next 
# variables and datatypes
# variable antey enti antey 
# it is used to store a data 

# datatypes 
# in this we have 2 types 1 is primitive & 2 is non primitive
# 1 primitive , in this we have int,float,str,complex,boolean 
# this primitive dt r immutable tha means we can't change the values 
# add and values and remove the values we don't do it in this pdt's
# age = 10 this is int kavali anukutey ila ivu 
# print(type(age)) class 'int' anni vastadi
# pi = 3.19 this is float same as print(type(pi))
# a = 'python' this is str print(type(a))
# b = True this is boolean print(type(b))
# non primitive taravatha chudam
# 
# 
# ippudu basic input/output antey ento chudam
# output antey print('hello') ila istey hello anni op vastadi
# input antey manamu user ni input enter cheyamani adagachu , adi 
# default ga string lo untadi nuv number ivali anukuntey j = int(input)
# ila ivali 
# a = input('enter ur name :')
# print('hello',a) like this 

# next vachi comments  we give # for commenting a single line r multiple lines
# or we use quotes ''' matter ''' like this 

# vitti medda code radamu
# age = 22
# name = 'ravi varma'
# percentage = 7.16
# a = True
# print(f' my name is {name} , age is {age} and my btech percentage is {percentage} , this all matter is {a}')

# Age=22
# print(Age)

# a=10
# b=20
# print(id(a))
# print(id(b))


# a= 10.5
# print(type(a))

# a = True
# print(type(a))

# non primitive 
#  list 2 tuple 3 sets 4 dict
# list : it is a collection of homogenous and non - homogenous data
#  homogeous (1,2,3,4) , ('ravi','sai')
# non homogenous (1,2,3,'ravi','sai',10.7)
#  it is denoted by [] is it square 
# a = [1,2,3,'sai',123]
# print(a)
# methods 
# 1 append 2 remove 3 clear
# a = [1,2,3]
# a.append(7) 
# print(a)

# 2 remove : it will remove praticular value , in this we give only 1 value
# b = [1,2,3,5,'ravi','sai']
# # b.remove(2) one oka argument ne remove cheystadi
# print(b)

#3 clear : it is used to clear all the list , it will return only [] this 
# c=[1,23,45,67]
# c.clear()
# print(c)

# 4 copy : it is used to copy a list in a new list
# d=[1,2,3,4,5,6]
# p=d.copy()
# print(p)

#5 count : it is used to count the praticular value ans count it
# f=[1,2,3,4,1,1,1]
# x=f.count(1)
# print(x)

# 6 extend : indulo multiple values nii rasukovachu
# a=['sai','ravi','ram']
# b=['chandu','krish','venkat','srinu']
# a.extend(b)
# print(a)

# index : to represent the index value in a list
# fruits = ['apple', 'banana', 'cherry']

# w=fruits.index("cherry")

# print(w)