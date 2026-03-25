#print all even numbers from 40 to 20 in rev order
#print all odd numbers from 30 to 10 in rev order
#find sum of squares of all odd numbers from 1 to 20
#find sum of all even numbers from 20 to 40

#1.
# for i in range(40,20,-2 ): #rev lo kabbati -2 pettali and start lo big num untey step lo - num vundali..
#     if i%2==0:
    #  print(f'{i} is even number')
# for even in range(40,20,-2):
#     print(even)

#2.
# for v in range(30,10,-1):
#     if v%2!=0:
#         print(f'{v} is odd number')
# for s in range(29,9,-2):
        # print(s)

3.
# sum=0
# for i in range(1,20):
#   if i%2!=0:
#     sum+=i**2
# print(sum) #print bhayata ichamu kabbati only one num a e

#3.
# sum=0
# for i in range(1,20):
#   if i%2!=0:
#     sum+=i**2
#     print(sum)

# #4.find sum of all even numbers from 20 to 40
# sum=0
# for i in range(20,41,2):
#     sum+=i
# print(sum)

#<<<<<<<<<<<<<TASK>>>>>>>>>> <<<<<<<<<<<<<<<<<<END>>>>>>>>>>>>>>>>>>>>>

#LOOPS :-
#loops are used to execute a block of code repeatedly , or we use it specific num of times , while a condition is true..
#in this we have 2 types 1.for loop 2.while 

#for loop

#example:-
# for i in range(5):
#     print(i,'hello') 
# op:-hello
#      hello
#      hello
#      hello
#      hello

#in this we have starting , ending , step options , we will give those r in range like this
#(1,       10,    1)
# |        |      |
# start    end    step lets run this
# for s in range(1,10,1):
#     print(s)
#op:-1 :- start num 1 ichamu 1 vachindi
# 2 
# 3
# 4
# 5
# 6
# 7
# 8
# 9 end eppudu , niku kavalisina num kana oka num +1 ivali 10 istey 9 vastadi 11 istey 10 vastadi 
# step 1 ichanu antey akkada oka step tisukuntadi , so gap rakunda line ga tisukuntadi..
# inkokati (1,20,1) eppudu kuda small big num istey step + lo tisukovali lekkaote print avadhu.

# for laptop in range(30,1,-1):  #(30,1,0) ila isety :-arg 3 must not be zero 
#     print(laptop) 
# #op:-reverse lo print avutadi like 30 nuchi 2 dakka just oka 1 step tho ,& ikkada start big num tisukunte
#step - lo tisukovali..

# for ravi in range(1,20):
#     print(f'{ravi} hello') #start 1 nuchi icahmu soo 19 dakka hello anni vastadi..

# a=10 intial eppudu 0 undali , nuv entha ichina vast loop +=a anni istey 0+1 anni tisukuntadi 
# for a in range(1,20):
#     a+=a
#     print('sorry') 19 times sorry print avutadi...


# x=5
# for v in range(5):
#     x+=1
#     print(x) #op 6- 10 print avutadi 
#print indentation lekkunda istey 10 print avuadi..

# a="apple"
# for i in a:
#     print(i)

# a="ravivarma"
# for b in range(1,5):
#     print(b)

# <<<<<<<<<<<SUMS>>>>>>>>>>>>>

#sum

# sum=0
# for c in range(1,11):
#    sum+=c
# print(sum) op:=55

# sum=0
# for c in range(1,11):
#    sum+=c
#    print(sum) :=1,3,6,10,15,21,28,36,45,55

# sum=0
# for i in range(1,10):
#      sum+=i**2 #op:=1,5,14,30,55,91,140,204,285
#      print(sum)

# sum=0
# for i in range(1,10):
#     sum+=i**2
# print(sum) #op:=285 

#<<<<<<<<<<<<<<<<TABLES USING FOR LOOP>>>>>>>>>

# for i in range(1,22):
#     print(f'2X{i}={2*i}') 

#<<<<<<<<<<<<<<<<TABLES USING FUN WITH FOR LOOP>>>>>>>>>>>>>>>.
# def table(x):
#     for i in range(1,21):
#         print(f'{x}X{i}={x*i}')
# table(5) #20 dakka 5 table print avutadi

# What is i? for i a: 
# i is a loop variable that takes on the value of each character in the string a one by one.

#for in lists[]
# a=['ravi','varma','siva']
# for i in a:
#     print(i)

# a=['ravi','varma','siva',289,82]
# for i in a:
#     print(i)

# list=['ntr','msd','kajal']
# for ravi in list:
#     # print(ravi)
#     if ravi=='kajal':
#         print('jai hind')
#     elif ravi=='ntr':
#         print('actor')
#     elif ravi=="msd":
#         print('cricketer')

#square of num in for looop

# numbers=[9,3,5,7,8,2,4]
# for squ in numbers:
#     print(squ**2)

#reversed a string..
# name='mom'
# rever_name=''
# for i in name:
#     rever_name=i+rever_name
# print(rever_name) 

# for s in range(1,8):
#     if s==1:
#         print('wake up at 6:00am')
#     elif s==2:
#         print('bathing at 7:00am')
#     elif s==3:
#         print('going to temple at 8:00am')
#     elif s==4:
#         print('eating my tiffin at 8:30am')
#     elif s==5:
#         print('going to istitute')
#     elif s==6:
#         print('listening the python class')
#     elif s==7:
#         print('listening html class')
#     else:
#         print(' need to improve')

# for _ in range(7):          # Outer loop runs 7 times (the schedule repeats 7 times)
#     for s in range(1, 8):   # Inner loop runs from 1 to 7 to print each activity
#         if s == 1:
#             print('wake up at 6:00am')
#         elif s == 2:
#             print('bathing at 7:00am')
#         elif s == 3:
#             print('going to temple at 8:00am')
#         elif s == 4:
#             print('eating my tiffin at 8:30am')
#         elif s == 5:
#             print('going to istitute')
#         elif s == 6:
#             print('listening the python class')
#         elif s == 7:
#             print('listening html class')
#     print()  # blank line between each repetition for clarity

#repu sir ni adugu

#using for loop

# a=(1,2,3,44,22,12,14,15,16,17,20)
# for b in a:
#     if b%2!=0:
#         print(f'{b}is odd number')

# a=[1,2,3,44,22,12,14,15,16,17,20]
# sum=0
# for b in a:
#     if b%2==0: #loop lo emi variable ichamo adey ivali
#         print(f'{b}is odd number') #formatting f print use cheyali
#     sum+=b #ikkada eppudu sum a starting ivali
# print(sum) #indulo sum a print cheyali..

# a=['list','ravi','varma','raju','ram']
# #  a='1'
# for i in a:
#     if i==a[3]: #condition true ayindi kabbati manaki nachina str ni or name ni index ichi prinnt cheysukovachu..
#      print(f'{a[1]}') #condition lekkapoyina ila ichamu kabbati 1 index lo ravi undi adey 5 times print avutadi coz list len is 5
#  break #istey okasarey print avutadi...

# 1.sum of even nums
# n=[1,2,3,4,5,6,7,8]
# sum=0
# for even in n:
#     if even%2!=0:
#         print(f'{even} is a odd num')
#         sum+=even 
# print(sum)

# a=input('enter the name:')
# vowels='a','e','i','o,''u'
# count=0
# for i in a:
#     if i in vowels:
#         # print(i)
#         count+=1
# print((i),count)

# ab=int(input('enter a num:'))
# for i in range(1,11):
#     print(f'{ab}x{i}={ab*i}')

#<<<<<<<<<<<LIST >>>>>>>>>>>>>
# tple=('hi','hello','bye',4,5,8,9)
# b=('tata','bye')
# for i in tple: rev cheyali antey range tisukuni (len(tple)-1,-1,-1)
#     b+=tple
#     break
# print(b) tple[i]

#<<<<<<<<<<<<SET>>>>>>>>>>>>>>>
# se={'helo','rey',4,4,5,7,'helo'}
# for i in se:
#     print(i)
#ikkada prat sari values change avutai coz of hasing , random key same order radhu diff ga untadi 
#purpose of thisis security purpose like otp's

#<<<<<<<Dictionaries>>>>>>>
# ditc={'product_name':'hp',
#       'price':'56000',
#       'ram':'16kb',
#       'color':'pink'
#       }
# for i in ditc:
#     print(i,ditc[i]) #or i or ditc[i]

# All dictionaries have the same keys: 'name', 'age', 'email'

# people = [
#     {'name': 'Alice', 'age': 28, 'email': 'alice@example.com', 'price': 19},
#     {'name': 'Bob', 'age': 34, 'email': 'bob@example.com', 'price': 24},
#     {'name': 'Charlie', 'age': 25, 'email': 'charlie@example.com', 'price': 17},
#     {'name': 'Diana', 'age': 31, 'email': 'diana@example.com', 'price': 21},
#     {'name': 'Ethan', 'age': 29, 'email': 'ethan@example.com', 'price': 22}
# ]
# for i in people:
#         print(i['price'])
    # print(i['name'])
    # print(i['price'])
# for x  in people:
#     if (x["price"]>10 and x["price"]<19):
#         print(x)


#<<<<<<<<<#PRIME NUMBERS>>>>>>>
2,3,5,7,11,13,17,19

# a=1
# p=0
# for i in range(1,a+1):
#      if a%i==0:
#          p=p+1
# if p == 2:
#     print('prime num')
# else:
#     print('not prime')


# a=int(input('enter the number='))
# ravi=0
# for i in range(1,a+1):
#     if a%i==0:
#         ravi=ravi+1
# if ravi==2:
#     print(f'{a} is a prime')
# else:
#     print(f'{a} is not a prime')

#<<<<<<<< PERFECT NUMBER >>>>>>>>>
#perfect num antey ippudu oka num undi
#example 6 undi diniki 1tho kuda div avutadi 2tho div avutadi 3tho avutadi 6tho avutadi
#and 1+2+3=6 ila kuda ravai
# a=(input('enter a num:'))
# b=0
# for i in a:
#     if a%i==1 and a%i==2 and a%i==3:
#         print('perfect squ')
#         b=a+1
#         print(b)

#using with end
# l='ravivarma'
# for a in l:
#     print(a,end='')

#without using end
# a='ravi varma'
# b=''
# for aa in a:
#     b=b+aa
# print(b)
# print('end')

#Ippudu oka  str=ravivarma anni undi indulo naku only i a print cheydam anukuntuna ala
# c='ravi varma'
# for a in c:
    # if a=='a': #check cheystadi a=a vastey 
    #     print('a is found') #a found vachi
        # continue
#     print(a) #print avutadi
# # if a == 'a' → ✅ True

# It prints: a is found

# continue tells Python: ❌ "Skip the rest of this loop and go to the next character"

# So it does not run print(a)

# ⛔ 'a' is not printed.

# b='sivasubba'
# for x in b:
#     if x=='a':
#         print('hi')
#         continue
#     print(x)
# Rule of Thumb:
# If you want to do something for each character, keep it inside the loop.
# If you want to do something after the loop finishes, put it outside. a

# ✅ 1. Print vowels in a string
# Q: Given a string "education", print only the vowels (a, e, i, o, u).

# a='education'
# b='aeiou'
# for i in a:
#     if i in b:
#         print(i)

#  2. Count how many times 's' appears
# Q: Given word = "sassy stone", count how many times the letter 's' appears.

# word='sassy stone'
# count=0
# for a in word:
#     if a=='s':
#         count+=1
# print(count)

# 3. Print each item in a list
# Q: Given fruits = ['apple', 'banana', 'cherry'], print each fruit on a new line.
# fruits=['apple','banana','cherry']
# for a in fruits:
#     print(a)
 
#  4. Print only numbers greater than 10
# Q: Given numbers = [4, 12, 7, 15, 3, 22], print only the numbers greater than 10.
# num=[4,12,7,15,3,22]
# for i in num:
#     if i>10:
#         print(i)

#  5. Skip specific item in list
# Q: Given colors = ['red', 'blue', 'green', 'yellow'], print all colors except 'green'.

# colors=['red','blue','green','yellow']
# for s in colors:
#     if s=='green':
#         continue
#     print(s)

# 6. Print characters but stop at 'm'
# Q: Given word = "programming", print one character at a time. Stop if the letter is 'm'.
# word='programming'
# for k in word:
#     if k=='m':
#     #  if 'm' in k:
#         break
#     print(k)

# 7. Reverse a string manually
# Q: Given name = "python", use a for loop to print the characters in reverse order. (Hint: don't use reversed() or slicing)
# name='python'
# a=''
# for i in name:
#     a=i+a
# print(a)

# # 8. Print unique characters in a string
# # Q: Given text = "success", print each character only the first time it appears (avoid duplicates). 
# text='success'
# b=''
# for i in range(len(text)):
#     if text not in b:
#         b=b+text
#         print(b)

#factorial
# a=1 # a=1 
# for i in range(1,6):# i=1 i=2 i=3 i=4 i=5
#     a=i*a # a=i*a.> 1*1=1 2*1=2  i=3 a =2 3*2=6 4*6=24  5*24=120
# print(a)



#while loop
#a wl is repeatedly executes a block of code as long as a specified condition is true
#syntax
#while condition / expression :
# block of code

# while True:
    # print('hello')

# a=1
# while a<=2: #ikkad 2 ichav anuko 2 jai hind print avutadi..
#     print('jai hind')
#     a+=1

# a=10
# while a>0:
#     print('python')
#     if a==10:
#      print('java')
#      a-=10
# else:
#     print('python & java')

# a=2042
# while  a:
#     if a%2==0:
#         print(a,'is a even num')
#         break
# else:
#     print('malli chudu')

# a=1
# while a<=20:
#   if a%2==0:
#      print(a,'is a evn number')
#   a+=1
# else:
#    if a%1==0:
#       print(a,'is odd num')

# name=input('enter ur name:')
# while name!='ravi': #ravi istey condition flase ayyi else block kiii veltadhi
#     print('my name is',name)
#     name=input('enter ur name:')
# else:
#     print('enter any name rether than ravi')
       

     

# What it does:
# It asks the user for a new name on each loop.
# It updates the value of name.
# If the new input is 'ravi', the loop ends.

#ekkada nuchi start cheyali and ekkada nuchi end cheyalo kuda while ki cheypali..

# n=int(input('enter a number:'))
# b=0
# while n>0 and n<=5:
#     b=b+n
#     n=n-1
# else:
#     if b==0:
#      print('given numbers only for 1 to 5')
# print('sum is',b)

# x=int(input('enter a number:'))
# a=0
# while x>0:
#     a=a+x
#     x=x-1
# print('sum is',a)

#to  print while loop in even or odd
# a=int(input('enter a number:'))
# while a%2==0:
#     print(a,'is a even number')
#     break
# else:
#     print(a, 'is odd number')


#to print additon of 2 numbers with while loop
# a=20
# b=30
# while a<b:
#     print(a+b)
#     break

#to print multiple of 5 number in a list
# list=1
# list2=3
# sum=1
# while list<list2:
#     sum=list*list2
#     print(sum)
#     if sum==3:
#      print('loop ends')
#      break
#     # break #if u not giving break loop runs until the condtion is false

# num = 7989740659
# while (num>0):
#    id = num%10
#    print(id)
#    num=num//10

# bbday=True
# b=0 writing sepeartely from where to start
# while(bbday and b<=5): adding condition
#     print('offers')
#     b=b+2 updating seperately in block of code

# x=0
# while (x<=20 ):
#     print(x)
#     x+=2 

# x=1
# while (x<=20):
#     print(x)
#     x+=2

#to print even or even
# x=1 #or 2
# while (x<=20):
#     if (x%2==0):
#         print(x, 'is a even number')
#     x+=1 # increment if istey dai kinda undeley na chusuko


