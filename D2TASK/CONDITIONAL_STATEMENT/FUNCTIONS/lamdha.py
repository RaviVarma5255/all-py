# lambda functions antey anti 
# a lambda funtion is a small , anonymous fun in py
# it is used when you need fun for a short period and don't want to formally define it using def.

# syntax
# lambda arguments: expression
# here lambda is keyword 
# arguments is : input parameterrs (can be multiple , spearated by commas)
# expression : single expression whose result will be returend automatically.

# a=lambda a,b: a+b
# print(a(1,3*3))

# b=lambda v,e,w: v+w*e
# print(b(1,5,10))

# Summary

# b → variable holding a function.

# v, e, w → parameters (placeholders).

# 1, 5, 10 → arguments (actual values).

# Expression (v+w*e) → runs with give

# c= (lambda a: 's' if a>10 elif a<=5  else 'no') 
# print(c(20))
# mannamu if and else a use cheyagalammu but elif use cheyalemu 
# but antha ga cheyali anukuntey nest conditional expression rasukuntam

# conditions rayali antey
# mundey output manamu ivali str lo
# chudam alano
# a=lambda c: 'hello' if c>=20 else 'hi'
# print(a(50-10*20-100)) op:hi
# nums = [1, 2, 3, 4, 5]

# result = list(map(lambda x: x*2, nums))
# print(result)

# nums = [1, 2, 3, 4, 5]

# result = list(map(lambda x: x*2, nums))
# print(result)

# Step 2: How x gets values

# Your lambda defines a parameter called x.

# When map runs, it takes elements of nums one by one and assigns them to x.

# So the connection is:

# 1st element of nums → x = 1

# 2nd element of nums → x = 2

# 3rd element of nums → x = 3

# 4th element of nums → x = 4

# 5th element of nums → x = 5


# Step 3: Apply lambda for each x
# lambda x: x*2


# If x = 1 → result = 2

# If x = 2 → result = 4

# If x = 3 → result = 6

# If x = 4 → result = 8

# If x = 5 → result = 10

# So finally → [2, 4, 6, 8, 10].


# ✅ Key Idea

# You are correct:

# x does not belong to nums directly.

# Instead, map is the “middleman” → it takes elements from nums and passes them to x in your lambda.

# a=lambda *v: max(v) 
# print(a(10,20,30,40,50),a(20,30,40))

# What ** does

# *args → collects values into a tuple

# **kwargs → collects keyword arguments into a dictionary

# 👉 kwargs stands for keyword arguments.

# 🔹 Example: **kwargs in normal function
# def greet(**kwargs):
#     print(kwargs)

# greet(name="Ravi", age=22)
# # Output: {'name': 'Ravi', 'age': 22}


# name="Ravi" → key = "name", value = "Ravi"

# age=22 → key = "age", value = 22

# All packed into a dictionary.

# 🔹 Example: **kwargs in lambda
# f = lambda **kwargs: kwargs
# print(f(city="Hyderabad", lang="Python"))
# # Output: {'city': 'Hyderabad', 'lang': 'Python'}

# 🔹 Accessing specific values
# f = lambda **kwargs: f"Hello {kwargs['name']}, you are {kwargs['age']} years old."
# print(f(name="Ravi", age=22))
# # Hello Ravi, you are 22 years old.

# 🔹 Combining *args and **kwargs
# f = lambda *args, **kwargs: (args, kwargs)

# print(f(1, 2, 3, name="Ravi", lang="Python"))
# # ((1, 2, 3), {'name': 'Ravi', 'lang': 'Python'})


# ✅ So, ** is used when you want your function (or lambda) to accept any number of keyword arguments, and they get packed into a dictionary.

# Do you want me to also show you how to unpack * and ** when calling functions? (that’s the opposite of collecting).

# lambda lo manamu conditons lo elif statement use cheyalemu and alagey ekkuva conditions use cheystey code messy ga untadi ..
# so vatti place lo map filter and reduse use cheystamu
# kavali antey nested if use cheyachu 
# example
# check_num = lambda x: "Zero" if x == 0 else ("Positive" if x > 0 else "Negative")

# print(check_num(0))    # Zero
# print(check_num(10))   # Positive
# print(check_num(-5))   # Negative

# def a(b):
#     return b*b
# def square(func,b):
#     return func(b)
# print(square(a,8))


# <<<<<<<<<<<<<<<<< MANAMU LAMBDA LO FOR LOOP RAYALEMU VATTI PALCE LONEY MAP FILTER AND REDUCE USE CHEYSTAMU>>>>>>>>>>>>>>>>>>>>


# def sq(x):
#     return x**2
# def cb(x):
#     return x**3
# def pro(fun,a):
#     reulut=[]
#     for i in a:
#         sqs=fun(i)
#         reulut.append(sqs)
#     print(reulut)
# pro(sq,[1,2,3,4,5])
# pro(cb,[1,2,3,4])

# ila ee for loop anta kakunda simple ga map use cheyachu ela nooo chudam lee 


# def cal(fun,a,b):
#     op=fun(a,b)
#     return op
# op1=cal(lambda a,b : a-b ,4,5)
# op2=cal(lambda a,b:a*b,3,3)
# op3=cal(lambda a,b: a/b,10,2)
# print(op1)
# print(op2)
# print(op3)

# li=['ravi','varma','siva','subba']
# a=map(lambda v:v+' '+'hello' ,li)
# print(set(a))

# What is map()?
# map() applies a function to every item in an iterable (like a list, tuple, etc.) 
# and returns a map object (which can be converted to a list).
# Syntax:

# map(function, iterable)
# ila for loop use cheysukuni elements ki 4 add cheysi b lo total chupistadi
# a=[1,2,3,4,5,6]
# b=[ ]
# for i in a:
#     b.append(i+4)
# print(b)

# # ippudu lambda lo map chesukuni ela no chuudam
# q=[1,2,3,4,5]
# v=map(lambda s:s+10 ,q)
# print(list(v))

# 1️⃣ Lambda function structure

# A lambda is just a small anonymous function:

# lambda parameters: expression

# parameters → like variables in normal function, e.g., x, s, a, b

# expression → what you want to return automatically, e.g., x + 10, a*b

# Example:

# f = lambda x: x + 10
# print(f(5))  # 15

# x is the parameter

# 5 is the argument

# x + 10 is the expression

# 2️⃣ How map works with lambda
# q = [1, 2, 3, 4, 5]
# v = map(lambda s: s + 10, q)


# lambda s: s + 10 → s is parameter, s + 10 is expression

# map takes each element of q as argument and passes it to s

# 1 → s = 1 → s + 10 = 11

# 2 → s = 2 → s + 10 = 12

# … and so on

# 1. Add Country Code to Phone Numbers
# Given phone numbers ["9876543210", "9123456780", "9988776655"], use map()
# to add +91- before each number.

# numbers = ["9876543210", "9123456780", "9988776655"]
# v=list(map(lambda v:'+91-'+v , numbers))
# print(v) 
# op: ['+91-9876543210', '+91-9123456780', '+91-9988776655']


# 2. Convert Prices from Dollars to Rupees
# Given product prices [10, 25, 40, 100] in dollars, use map() to convert them to 
# rupees (1 USD = 83 INR).

# dollars = [10, 25, 40, 100]
# rupees = list(map(lambda v:v*83 , dollars))
# print(f'{rupees} is the inr of dollars {dollars}')

# op = [830, 2075, 3320, 8300] is the inr of dollars [10, 25, 40, 100]

# 3. Mask Credit Card Numbers
# From ["1234567890123456", "9876543210987654"], use map() to mask them as 
# "************3456".

# x=["1234567890123456", "9876543210987654"]
# c=map(lambda v: '*' *12 +v[-4:],x)
# print(list(c))


# 4.Format Product Labels
# From ["apple", "mango", "orange"], use map() to format them as → "Product: 
# Apple".

# a = ["apple", "mango", "orange"]
# b=list(map(lambda c:'Product :'+c,a))
# print(b)

# a = ["apple", "mango", "orange"]
# c=map(lambda v:"Product :" +v[0].upper() + v[1:],a)
# print(list(c))

# ila kakunda 
# a = ["apple", "mango", "orange"]
# c = map(lambda v: "Product: " + v.capitalize(), a)  # capitalize first letter
# print(list(c))
# ila kuda rasukovachu

# or 

# fruits = ["apple", "mango", "orange"]
# formatted = list(map(lambda x: "Product: " + x.title(), fruits))
# print(formatted)
# ila kuda rasukovachu

# # <<<<<<<<<<<<<<<<<<<<<< FILTER >>>>>>>>>>>>>>>
# What is filter()?

# filter() is a higher-order function in Python.

# It filters items from an iterable based on a condition.

# Only the items that return True in the function are kept.

# syntax 
# FILTER(function,iterable)
# function → a function (normal or lambda) that returns True or False

# iterable → list, tuple, etc.

# Returns a filter object, which you usually convert to a list to see results.

# nums = [1, 2, 3, 4, 5, 6]

# evens = filter(lambda x: x % 2 == 0, nums)
# print(list(evens))
# filter ki condition ivali 

# s=[1,2,3,4]
# sum=filter(lambda c: c==4 ,s)
# print(list(sum))


# <<<<<<<<<<<<<<<<<<<<TASKS>>>>>>>>>>>>>>

# 1. Add Country Code to Phone Numbers
# Given phone numbers ["9876543210", "9123456780", "9988776655"], use map()
# to add +91- before each number.

# a=["9876543210", "9123456780", "9988776655"]
# b=map(lambda v:"+91-" +v , a)
# print(list(b))


# 2. Convert Prices from Dollars to Rupees
# Given product prices [10, 25, 40, 100] in dollars, use map() to convert them to 
# rupees (1 USD = 83 INR).

# dollars= [10, 25, 40, 100]
# rup=list(map(lambda x:x*83 , dollars))
# print(f'the inr ruppes of {dollars} is {rup}')


# 3. Filter Gmail IDs
# From ["harish@gmail.com", "abc@yahoo.com", "xyz@gmail.com"], use filter() to 
# keep only Gmail IDs.

# 4. Get Short Product Names
# From ["Pen", "Notebook", "Laptop", "Charger", "Bag"], use filter() to return names 
# with length ≤ 5.

# a=["Pen", "Notebook", "Laptop", "Charger", "Bag"]
# b=list(filter(lambda x: len(x)<=5 ,a))
# print(b)


# 5. Convert Names to Usernames
# From ["Harish", "Sushma", "Nandu"], use map() to convert into usernames 
# (lowercase with @gmail.com).
# → ["harish@gmail.com", "sushma@gmail.com", "nandu@gmail.com"]


# 6. Filter Expired Products
# Given product expiry years [2022, 2023, 2025, 2026], use filter() to keep only 
# expired ones (assume current year = 2025).
# v=[2022, 2023, 2025, 2026]
# c=list(filter(lambda c: c<2025,v))
# print(c,'is the expired ones')

# 7. Mask Credit Card Numbers
# From ["1234567890123456", "9876543210987654"], use map() to mask them as 
# "************3456".





# 8. Filter High Salary Employees
# From [25000, 45000, 60000, 15000, 80000], use filter() to return employees with 
# salary ≥ 40,000.
# s=[25000, 45000, 60000, 15000, 80000]
# m=list(filter(lambda o:o>=40000,s))
# print(m)

# 9. Format Product Labels
# From ["apple", "mango", "orange"], use map() to format them as → "Product: 
# Apple".

# 10. Students Passed
# From student marks [35, 80, 55, 20, 90], use filter() to return students who 
# scored ≥ 40.
# b=[35, 80, 55, 20, 90]
# w=list(filter(lambda l:l>=40,b))
# print(w)

# 11. Filter Strong Passwords
# From ["abc123", "Admin@123", "hello", "Pa$$word"], use filter() to return only 
# strong passwords (length ≥ 8 and must contain @ or $).

# k=["abc123", "Admin@123", "hello", "Pa$$word"]
# l=list(filter(lambda e: len(e)>=8 and '$' ,k))
# print(l)

# 12. Process Transaction Records
# Given transactions as ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"]:

# • Use map() to extract the amounts as integers.
# • Use filter() to separate credits and debits.
# a = ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"]
# n=list(filter(lambda e:e[5:]=='CREDIT' ,a))
# print(n)
