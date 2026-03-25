#CONDITIONAL STATEMENTS 
#statement which executes based on a specific condition then it can 
#be called as conditional statements..

#in this we have 5 types
#1 if 2 if else 3 nested if 4 elif ladder 5 

#1 IF..
#An if statement in Python is used to run a block of code only if a certain condition is true.
#if condition true ayiteney manaki if lo rasina condition print avutadi ..

#<<<<EXAMPLE>>>:-

# a=20
# b=20
# if(a==b): #== petali coz we comapring both .
#     # print("hello world")

# age=22
# if(age>=20): #>=20 antey 22 anndi 20 kan pedadi kabbati idi print ayindi ..
#     print("super")

# o='ravi varma'
# p='ravi varma'
# if(o==p): #o&p rendu same ichamu kabbati condition true..
#     # print('good')

# a=input("enter ur name:")
# if(a=='varma'):
    # print('rajulu') #ikkada input tisukuni print cheymantunam ..so condition lo ichina name &
# ^ #input ichina name correct ayitey naku op:-rajulu anni print avutadi.
#.INDENTATION.. antamu..(^) ee pyna space ni indentation ..

#2. else syntax ("The **else** statement in Python is used to define
#  a block of code that runS the if condition is False.)
# MANAKI ARDAM AYYEY BASALO :- IF CONDITION FALSE AYITEY , ELSE LO DI PRINT AVUTADI..

#syntax:-
#if condition:
    # runs if condition is True
#else:
    # runs if condition is False
#examples...

# a=20
# b=30
# if(a>=b):
#     print("chinta")
# else:
#     print("yeswitha")

# i=222
# k=222
# if(i!=k):
#     print("yeswitha")
# else:
#     print("chinta")

# m=31
# n=30

# if(n>m):
#     print("thaf")
# else:
#     print("loves") 


# u=20
# if(u<14):
#     print("monday tiffin is:-idly")
#     if(u>15):
#         print("tuesday tiffin is:-vada")
#         if(u==20):
#             print("wednesday tiffin is dosa")
#             if(u!=40):
#                 print("thursday tiffin is pillihora")
#                 if(u>=10):
#                     print("friday tiffin is vutapamu")
#                     if(u>16):
#                         print("saturday tiffin is chappati")
#                         if(u>=20):
#                             print("sunday tiffin is upma")
#                         else:
#                             print("day wise tiffins list")

#<<code for even and odd numbers>>
# a=int(input("enter a number:"))
# if(a%2==0): #ippudu nenu input lo 20 ichanu ,ikkada condition loo modulos 
#     print('even num') #2 ichi ==0 ichanu remainder 0 vastey if condition true avi excute avutadi ..20%2 antey 0
# else:
#       print('odd')


# b=input('enter the name:')
# if(b=='raju'):
#     print('9391443569 is raju num')
# a=input("enter the name of raju's son:")
# if(a=='ravi'):
#     print(7989740659)
# d=input('enter the dagu name of raju:')
# if(d=='srav'):
#     print(81234710)
# else:
#     print(123456789) #ikkada anni conditions true ayipotayi coz condition ala tisukunam

# a = 330
# b = 330

# print("A") if a > b else print("=") if a == b else print("B")


# <<<<<<< code >>>>>>>
# x = 13

# if x > 5:
#     print("Outer if: x > 5")
 
#     if x > 15:
#         print("Inner if: x > 15")

#     elif x > 10:
#         print("Inner elif 1: x > 10")  # This block runs

#         # Now write more logic INSIDE this elif
#         if x>11:
#          if x % 2 == 0:
#              print("Nested if inside elif: x is even")
#          elif x %2 ==1:
#              print("Nested elif inside elif: x is odd")
#              if x>10:
#                 if x%3==0:
#                     print('it is not divisible by 3')
#                 elif x>12:
#                     print('hello') 
#                     if x>81:
#                         print('cs')
#                     elif x<20:
#                         print('ss')
#                     else:
#                         print('nothing')
#                 else:
#                     print('hi') 
#          else:
#              print('huuu')    
# else:
#     print('lulu mall')


# is_login = True
# log_role = 'user'
# if(is_login):
#     if (log_role=='user'):
#         print('hello')
#     else:
#         print('zuzu')
#     if len(log_role) == 5:
#         print('hello')
#     else:
#         print('hi')
# else:
#     print('neruchuko')

# a='hello my name is ravi' 
# b=[]
# if 'hello' in a:
#     b.append('hello')
#     if 'MY' in a:
#         print('nothing')
#     elif 'my' in a:
#          b.append('my')
#          if 'R' in a:
#             print('nothing')
#          elif 'name' in a:
#             b.append('name')
#             if 'IS' in a:
#                 print('nothing')
#             elif 'is' in a:
#                 b.append('is')
#                 if 'V' in a:
#                     print('nothing')
#                 elif 'ravi' in a:
#                     b.append('ravi')
# print(b)

        
        
# a = 'madam'

# if a[0] == a[4] and a[1] == a[3]:
#     print('It is a palindrome')
# else:
#     print('Not a palindrome')

# a='mom'
# b = ''
# for i in a:
#     b=i+b
# if a == b:
#     print('it is a palindrome')
# else:
#     print('it is not palindrome')



# a= 20
# b=30
# if a < b:
#     print('helo')
#     if a==10+10:
#      print('kk')
#      if a==20:
#        print('nested if')
#      elif b==40-10:
#        print('jgvj')
#        if b==30:
#           print('jgh')
#        elif a<b:
#           print('ammo')
#     print('bye')
# else:
#     print('no signal')


# a=0
# b=1
# if a<b:
#     print('gn')
#     if a<b:
#         print('hel')
#         if a!=b:
#             if b!=a:
#                 print('ll')
#             elif b==1:
#                 print('jeo')
# #     if a==0:
# #       print('jj')

# x = 10
# if x !=10:
#     print('keep pratice')
# else:
#     print('lu lu mall')


# for i in range(1,10,9):
#     print('hello' , i)










