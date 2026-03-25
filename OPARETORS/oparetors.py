#"OPARETORS"

#it is a symbol which is used to manipulate data ..
# in this we have 7 types ...

#1 ARITHEMATIC 2 COMPARISON/RELATIONAL 3 LOGICAL 4 ASSIGNMENT 

#ARIITHEMATIC OPARETORS..
#IT PERFORMING MATHEMATICAL CALCULATIONS ON NUMERICAL VALUES. 
#IN THIS WE HAVE 1 ADDITION (+) 2 SUBTRACTION(-) 3 MULTIPLICATIO(*) 4 DIVISION(/) 5 MODULUS(%) 6 EXPONENTIATION(**) 7 FLOOR DISVION(//)

a=10
b=20
c=a+b  #additiion
# print(c)
# print(a-b) #subtraction
# print(a*b) #multiplication
# print(a/b) #division
# print(a**b) #exponenal
# print(a//b) #floor division
# print(a%b) #modulo

#2 COMPARISON /RELATIONAL OPERATOR
#in this we have 1 equal to(==) 2 not equal to(!=) 3 greater than (>) 4 less then (<) 5 GT OR Equal to(>=) 6 LT OR Equal to(<=)

#USED TO COMPARE 2 VALUES & RETURN A BOOLEAN RESULT TRUE OR FALSE

d=20
e=25
f=d==e #eqaul to #false .
# print(f) 
# print(e==d) #eqaul to #false .
# print(d!=e) #not equal to #true .
# print(e!=d) #not equal to #true  .
# print(d>e)  #greater than #false .
# print(e>d)  #greater than #true .
# print(d<e)  #less than #true .
# print(e<d)  #less than #false .
# print(d>=e) #greater than or equal too #false .
# print(e>=d) #greater than or equal to #true .
# print(d<=e) #less than or equal to #true .
# print(e<=d) #less than or eqaul to #false .

#TYPE 3
#LOGICAL OPERATOR 
# IN THIS WE HAVE and,or,not operatores ..

#AND kii rendu conditions true ayyi nappudey aa condition true print cheystadi ..

g1=30
g2=40
g3=(g1<g2 and g2>g1) #ikkada emi cheysamu antey rendu conditions true valey la cheysukunamn..
# print(g3) 
# print(g1<40 and g2==40) #true # ikkada true enduku print ayindi antey g1<40 icah so g1 value 30 kabbati  a condition true # g2==40 ichamu adi kuda correct
# print(g1==g2 and g2==g1) #false coz both conditions r false
# print(g2!=g1 and g1!=g2) #true 
# so and ki both condition true ivsali ..

#2nd operator vachi OR(or)
#indulo oka true unna gani true a 

x=50
y=60
z=(x<50 or y>60) # both condition loo oka true kuda ledhu kabbati false op vastadi #false
print(z)
# print(x==50 or y==60) #both true ichamu kabbati #true op vastadi
# print(x<60 or y>61) #first condition true kabatti #true op vastadi.. 

#3rd operator vachi not
#not loo true ithey false , false antey true op vastadi..

k=10
l=15
m=(not l==k) #edi false kabbati true print ayindi
# print(m)
# print(k !=l) #iddi false kabbati true print ayindi
# print(not l>k) #false
# print(not l<k) #true..

#type4 
#ASSIGNMENT OPERATORS..
#AO IS USED TO ASSIGN VALUES TO VARIABLES...
#BASIC ASSIGNMENT OPERATOR
#X=5

#COMPOUND AO

x=10
x+=10
# print(x) #addition cheysamu
# q=20
# q-=10 #minus cheysamu..
# print(q)
# w=30
# w*=2 #given num into 2
# print(w)
# t=40
# t/=2 #division 
# print(t)
# u=50
# u//=4 #ikkada float values chupinchadu 
# print(u)
# h=21
# h%=2
# print(h) #remiander
# z=30
# z**=2
# print(z) #square of given num

#type5 

#Bitwise operators :- it operators bit by bit on data 
#bit stands for binary digit ,it represents smallest value of a data..

#in this we have 1.bitwise and (&) 2.bitwise or(|) 3.bitwise xor(^) 
# #4. bitwise not(~) 5.left shift(<<) 6. right shift(>>)
#bitwise and(&) same as logical and but sybol ivali (&)
a=5
b=3
#print(a&b) 
#output 1 vastadi , ela vachindi antey . 5 ki binary value vachi 0101 and 3ki BN 0011 
#ippudu and , rendu conditions ture untey op kuda true vastadi .
# 0101
# 0011
# 0001 #ila vastadi 
#ila kakunda ila kuda cheyachu 
c=5
d=5
#print(bin(c&d))  #op #bin101 

#dobule digit...
e=20
f=30
#print(e&f) #op 20 ela antey 
#   16  8  4  2  1 
#20;-1  0  1  0  0
#30:-1  1  1  1  0
#    1  0  1  0  0 .....
#print(bin(e&f)) #op:- 0b10100 ...

#2.BITWISE OR(|)
# condition lo oka true ayina true a 

i=50
k=60
# print(i|k)
#     32 16 8 4 2 1 
#50:- 1  1  0 0 1 0
#60:= 1  1  1 1 0 0
#op:-  1   1   1  1  1 0 ans :- 62..

# print(bin(i|k)) #op:- 0b111110 

#3.BITWISE XOR(^)
q=10
w=20
# print(q^w)
# print(bin(w^q))
#      16 8 4 2 1
#10:-   0  1 0 1 0
#20:-   1  0  1 0 0
#op:-   1  1  1 1 0 ans :-30

#4. BITWISE NOT (~) NEGATION
# TRUE AYITEY FALSE , FALSE ANTEY TRUE ..
o=20
p=30
# print(~o)
# print(~p)

k=61
# print(~61)
# print(bin(k))

#emi kadhu just oka num tisukunav 21 daniki ~ 21 icahv ans vachi -22 ala a num tisukuna +1 add avutadi 
#but a value minus(-) lo vastadi

#5.BITWISE LEFT SHIFT (<<)
x=7
y=2
# print(x<<y)
#the zeros will be add right side 
# take box like 8 nums 0|0|0|0|0|1|1|1 based on what we assign the value
#                     |0|0|0|1|1|1|0|0 
#                 128|64|32|16|8|4|2|1 now add all 1's places 
# soo now 16+8+8 = 28 op:- 28 
d=7
g=5
# print(g<<d)
i=-6
l=1
# print(i>>l)

m=-8
n=1
# print(m>>n)

v=-9
c=1
# print(v>>c)

a=-22
b=1
# print(a>>b)

k=-33
l=1
# print(k>>l)

x=-11
y=1
# print(x>>y)

w=-77
h=1
# print(w>>2)

#6.BITWISE RIGHT SHIFT (>>)
j=5
k=2
# print(j>>2) 
#the zeros will be add left side..
# take box like 8 nums 0|0|0|0|0|1|0|1 based on what we assign the value
#                      0|0|0|0|0|0|0|1
#                 128|64|32|16|8|4|2|1 now add all 1's places..
# akkada last lo 1 unna 0 tisukuntadi..

#TYPE 6 :- BITWISE Identity 
# #Operators in Python are used to compare the memory locations 
# of two objects—not just their values. #
# These are: 1. IS 2. IS NOT it will print boolen values..
#Exmaple
#IS OPERATOER..
t=10
j=10
# print(t is j) #ikkada both values oka id same kabbati op;-true 
# print(t is not j) #ikkada is not anni icahmu , op:-false

u=10
d="10"
# print(u is d) #op:- False ade ippudu is not istey true op vastadi
# print(u is not d) #op:- will be true. -5 NUCHI 256 DAKEY TRUE PRINT AVUTAI IS ISTEY , kunni CMP use cheyali

#2. IS NOT
a1=-3
b2="hii"
# print(a1 is b2) #op:- false
# print(b2 is not a1) #op:- true 

a=[1,2,3,4,5,6]
b=a
# print(b is a)

b3={"name":"ravi"}
b4={"name":"varma"}
# print(b3 is not b4) #op:- true..

n1=[2,3,4,5,6]
n2=[2,3,4,5,6]
# print(n1 is n2) #op:-false 

a=(1,2,3,4,5)
b=(1,2,3,4,5)
# print(a is  b) #op:-true cmp lo false , but false a correct

#TYPE 7: BITWISE MEMBERSHIP..
#Membership operators are used to test whether a value exists 
#in a sequence like a string, list, tuple, set, or dictionary..
#THIS ARE 2 TYPES .. 1 IN 2 NOT IN ..
#EXMAPLE..
#IN 
seq=1,2,3,4,4,5,6
# print(2 in seq) #op:-true

list=["name","class","room","sir","o"]
# print(list[2][1] in list)
# print( in list) 

tup=(1,2,3,"ji","ki","li")
# print(1 in tup) #op:-true
# print('ji' in tup)

sets={2,3,4,6,7}
# print(2 in sets) #op:-true


dits={"name":"ravivarma","class":"54r","city":"kakinada"}
# print('kakinada' in dits.values() )

#print("name" in dits) #here we see the key will be printing .. but not the value , how it will be printed..


#TYPE 2 NOT IN ..
gh1=('abc','def','ghi')
# print('hii' not in gh1) #op:-true

k=['ravi','varma']
# print('siva' not in k) #op:-true

l=['kii','ohhu','haha']
# print('kii' not in l) #op:-false enduku antey kii anadi l lo undii.

f=(72,'828r',73647,3129,79337,)
# print(73647 not in f) #:-false...




# a = 4
# b = 2
# if not a < b:
#     print("a is not less than b")

a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter 4th number: "))
# if b>a>c or c>a>b:
#     print(f'2nd big num {a}')
# elif a>b>c or c>b>a:
#     print(f'2nd big num {b}')
# elif a>c>b or b>c>a:
#     print(f'2nd big num{c}')
# else:
    # print(f'2nd big num {d}')
















