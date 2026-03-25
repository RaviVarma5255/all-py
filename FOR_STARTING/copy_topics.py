# today class on copy topics 
# in this we have 2 types 1 shallow copy denoted by copy.copy()
# if we perform this opretion on lists and ditc , we have to give those in nested type not in direct list or dict
# if we assgin and change in the one or more copy , the main copy and the chnaged copy will also be changed
# example
# import copy
# ditcs={'names':{'name':'ravi','age':22,'gender':'male'},'ok':'okk'}
# d1 = copy.copy(ditcs)
# d2 = copy.copy(ditcs)
# d1['names']['name']='varma'
# d2['names']['age']=23
# d1['ok']='good' ila istey just last lo dii chnage avudati coz ok annadi nested lo lehu kabbati adey nuv 
# NAME varma istey addi last lo add avutadi 
# {'names': {'name': 'ravi', 'age': 22, 'gender': 'male'}, 'ok': 'okk', 'name': 'varma'} like this

# print(ditcs)

# iddi okati istey chalu coz shallow lo oka copy ni change cheysina mottam anni refrecens anni chnage ayipoai so kabbati print(d1) & d(d2) avas
# aram ledhu
# example in lists
# l=[1,2,[2,4,6,8]]
# l1 = copy.copy(l)
# l2 = copy.copy(l)
# l1[0,1]=9,2  ikkada nuv only l1[0] gani 1 kani ivali list[index]= value iddi dinni meaning nuv ala istey 
# TypeError: list indices must be integers or slices, not tuple ila vastadi error
# # l1[2][0]=[9,9] ila istey 2 index lo unna 0th position kii change avutadi [1, 2, [[9, 9], 4, 6, 8]] is d op
# print(l)
# print(l1)

# exmaple 2
# d={'user':{'name':'ravi','score':4}}
# d1=copy.copy(d)
# d2=copy.copy(d)
# d1['user']['score']+=4
# print(d1) {'user': {'name': 'ravi', 'score': 8}}

# l=[12,[1,2,3,[2,4,5,[0,0,0]]],'ravi']
# l1=copy.copy(l)
# l2=copy.copy(l)
# l2[2]='varma'
# l1[1][3][0]=1 [12, [1, 2, 3, [1, 4, 5]], 'ravi']
# l3=copy.copy(l)
# l3[1][3][3][0]=1
# print(l1)
# print(l1) [12, [2, 2, 3, [2, 4, 5]], 'ravi']
# print(l2) [12, [2, 2, 3, [2, 4, 5]], 'varma']


# 2 is deep copy it is denoted by copy.deepcopy()
# it will not chnage the refrences , it will going deeply and changed only values
# example

# # example with ditc
# matches={'score':{'runs':150,'overs':5.5,'wickets':5}}
# ravi=copy.deepcopy(matches)
# varma = copy.deepcopy(matches)
# ravi['score']['runs']+=70
# varma['score']['wickets']+=2
# ravi['score']['overs'] = 7.1
# # print(ravi ,'runs of csk')
# # print(varma,'wickets of fall for csk')
# print(matches,'it will me the main code it will be change in deepcopy')

# example with list 
# l=[1,[3,2,1,0]]
# l.append(21)
# print(l)
# q=copy.deepcopy(l)
# q[2]+=22 
# print(q) [1, [3, 2, 1, 0], 43]
# print(l) [1, [3, 2, 1, 0], 21]

# l=[1,1,2,3,4,5,6]
# b=copy.deepcopy(l)
# print(l)
# l.sort(reverse=True)
# print(l)
# l.append(20)
# a=l.count(1)
# print(l)
# print(a)
# print(l)
# q=copy.deepcopy(l)

# print(q)

# inka sets and tuples kuda avutai antha but ivi saripotayi max
# lists and dictionaries lo ney ekkuva use cheystamu


# ippudu recursion 
# Recursion is when a function calls itself to solve a smaller version of a problem until it reaches a base case.
# Think of it like matryoshka dolls (nested dolls): each doll contains a smaller doll, and recursion works by peeling one layer at a time.

# Key Parts of Recursion
# Base Case – The condition where the function stops calling itself.
# Recursive Case – The part where the function calls itself with a smaller or simpler input.
# Without a base case, recursion will run forever and cause a stack overflow.
# a fuction calling itself 
# return ee funtion tho pattu ee return ni kuda call chey mantundhi
# def a(b,c):
#     return b+c
# print(a(2,4))
# print(a(3,4)) niku return kavli antey kachitam gaa print ivali lekkapote non vastadi

# def b(a):
#     return a*a
# print(b(1))
# print(b(4))

# def a():
#     return ('hello')
# print(a())

# def a():
#     b=20
#     # print(b)
#     return b
# print(a())

# factorial 5*4*3*2*1 = 120
# s=1
# # a=[1,2,3,4,5] with a list
# for i in a:
#     s=s*i
# print(s) 

# a=int(input('enter the num :'))
# b=int(input('enter the num :'))
# c=int(input('enter the num :'))

# if (a>b and a>c):
#     print(f'largest is {a}')
# elif(b>a and b>c):
#     print(f'largest is {b}')
# else:
#     print(f'largest is {c}')


# fabonocci series using Recursion
# general ga fabnocci antey last 2 numbers add ayyi number ravali 
# like 0 undi and 1 undi 0 + 1 = 1 now ee 1 and last 1 + avali 2 ippudu ee 2 and last 1 add ayyi 3 ila ravali 
# for i in range(1,11):
#     if i == 0


# import copy

# DIC = {
#     "score":{"runs" : 123,"wickets":3},"overs":5,"SPEED":80
# }

# bumrah = copy.deepcopy(DIC)
# SIRAJ = copy.deepcopy(DIC)
# bumrah["score"]["runs"],SIRAJ['score']['wickets']= 90,5
# SIRAJ["score"]["runs"],bumrah['score']['wickets'],bumrah["score"]["overs"]= 70,6,7
# print(bumrah)
# print(SIRAJ)
# print(DIC)


# pubg = ["harish",['hari','hari282'],['chandu','chadu'],'ravi','sai']
# copied = copy.copy(pubg)
# copied2 = copy.copy(pubg)

# copied[0]="lion"
# copied2[1][1] = "kiet yuvatha"

# print(copied)
# print(copied2)
# print(pubg)


# def greet():
#     print("hello") #without recurion its calls on one time
#     greet() #it is with recursion used to call a statement in inside the function the limit is 1000
# greet()

# def open_box(n):
#     if n>1:
#         print(f"inside another {n} box")
#         open_box(n-1)
#     else:
#         print(f"found gift box in {n} the box")
# open_box(4)


# def factorial(n):
#     if n<0:
#         raise("factorial of does not work negative value")
#     if n in (0,1):
#         return 1
#     return n*factorial(n-1)
# n= int(input("Enter the value: "))
# result = factorial(n)
# print(result)