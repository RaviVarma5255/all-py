# daily problem sloving tasks
# Day 1: Basics (Warm-up)
# Check if a number is even or odd.
# Check if a number is positive, negative, or zero.

# 1

# a=int(input('enter the number :'))
# if a%2==0:
#     print(f'the given number {a} is even')
# else:
#     print(f'the given number {a} is odd')

# 2 

# b=int(input('enter the number :'))
# if b > 0:
#     print(f'{b} is postive number')
# elif b == 0:
#     print(f'{b} is zero number')
# else:
#     print(f'{b} number is negative ')

# def a(b):
#     if b%2==0:
#         print('it is a even number')
#     else:
#         print('it is odd number')
# a(3)
# a(2)
# a(93283)

# def to_know_even_r_odd(a):
#     if a%2==0:
#         return 'even number'
#     else:
#         return 'odd number'
# print(to_know_even_r_odd(22),' is 22')

# s=''
# q=[1,2,3,4,5,6,7,8,9,10]
# for i in q:
#     if i%2==0:
#         print(f'{i} it is even number')
#         s=' '
#         print(s)
#     else:
#         print(f'{i} it is odd number')


# while True:
#     a=input('enter the name :')
#     if a !='ravi':
#         print(f'ur enterd name is {a} now number')
#         b=int(input('enter the number :'))
#         if b%2==0:
#             print('it is even number')
#         else:
#             print('it is odd number')
#     else:
#         print('plz enter the name , that is not equal to ravi')
    
# Easy level

# Print numbers from 1 to 20.
# for i in range(1,21):
#     print(i)
# Print all characters of your name one by one.
# a='ravi'
# for i in a:
#     print(i)
# Print all even numbers from 1 to 50.

# for even in range(0,51,2):
#     print(even,'is a even number')
# Print the multiplication table of 5.
# a=5
# for i in range(1,11):
#     print(f'{a}x{i}={i*a}')
# Print the sum of numbers from 1 to 10.
# sum=0
# for x in range(1,11):
#     sum+=x
# print(sum,'is the total sum')

# Medium level

# Given a list of marks [95, 88, 76, 67, 89, 92], print only the marks greater than 80.
# marks = [95, 88, 76, 67, 89, 92]
# for i in marks:
#     if  i >80:
#       print(i)
# Print the square of each number from 1 to 10.
# for i in range(1,11):
#     print(i*i)
# Count how many vowels are in the string "python programming".
# v="python programming"
# o='aeiouAEIOU'
# for i in v:
#     if i in o:
#         print(i,end=',')

# Print a list in reverse order using a for loop.
# l=[2,1,38,'ravi']
# for b in range(len(l)-1,-1,-1):
#     print(l[b])

# Given a list names = ["ram", "s-ita", "lakshman", "hanuman"], print names with more than 3 
# names = ["ram", "s-ita", "lakshman", "hanuman"]
# for i in names:
#     if (len(i))>3:
        # print(i)

# funtions
# def a(b,c):
#     return (b-c)
# print(a(22,9),' days left to go to home')


# def b(*c):
#    c='days to go to home'
#    print(v,c)

# for i in range(9,23):
#     while True:
#      a=int(input('enter today date :'))
#      if a == 9:
#       v=22-a
#       b(13)  
#       break
#      elif a == 10:
#        v=22-a
#        b(12)
#        break
#      elif a == 11:
#        v=22-a
#        b(11)
#        break
#      elif a == 12:
#        v=22-a
#        b(10)
#        break
#      elif a == 13:
#        v=22-a
#        b(9)
#        break
#      elif a == 14:
#        v=22-a
#        b(8)
#        break
#      elif a == 15:
#        v=22-a
#        b(7)
#        break
#      elif a == 16:
#        v=22-a
#        b(6)
#        break
#      elif a == 17:
#        v=22-a
#        b(5)
#        break
#      elif a == 18:
#        v=22-a
#        b(4)
#        break
#      elif a == 19:
#        v=22-a
#        b(3)
#        break
#      elif a == 20:
#        v=22-a
#        b(2)
#        break
#      elif a == 21:
#        v=22-a
#        print(v,'day to go home')
#      else:
#        print('intiki potunam royyi huu lulu mall')
#      break


# def a(*b):
#     print(b)
# a('hi this is ravi varma','my age is',22 ,'i am from kakinada','my phone is number',7989740759)
# a('lulu','ok ok')
a=0
b=['ravi','varma','siva']
for v in b:
    for ch in v:
        if ch == 'a':
            print(ch,v)
    
