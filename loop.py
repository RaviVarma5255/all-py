# 1.#even numbers (40,20) in rev
# for i in range(40,20,-2):
#     if i % 2 ==0:
#         print(f'{i} is even number')

# # 2.#odd numbers in rev
# for a in range(29,9,-2):
#     if a%1==0:
#      print(f'{a}is odd number')

# # 3.#sum of all odd nums from (1,20)
# sum=0
# for s in range(1,20,2):
#     sum+=s**2
# print(f'{sum} is the sum of odd nums for 1,20')

# #4.sum of all even num from 20 t0 40
# sum=0
# for i in range(20,41):
#     if i%2==0:
#         sum+=i
# print(f'{sum} is the sum of even nums for 20,40')
    


1.#print all even numbers from (1 to 100)
# for i in range(1,100):
#     if i%2==0:
#         print(f'{i} is a even number')

# 2. rev a str without using sliceing
b='python'
c=''
for x in b:
    c=x+c
print(c)

#3.calculate sum of the digits of a num
# a=int(input('enter a number:'))
# sum=0
# for v in range(1,a+1):
#     sum+=v
# print(sum)

#4. count the num of words in a given sentence
# a='sentence'
# b=0
# for c in a:
#     b+=1
# print(f'count of a is {b}')

#5 find the max num in a list
# list=[1,3,842,583,820]
# max=0
# for i in list:
#     if i>max:
#         max=i
# print(max)
    

#6 print nums divisible by boyh 3&5 from 1 to 100

# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print(f'{i} is divisibles of both 3 and 5')

#7 check if a string is a palindrome 
# a='mom'
# b=''
# for i in a:
#     b=i+b
# if a == b:
#     print('it is a palindrome')
# else:
#     print('it is not palindrome')

# for i in range (1,20,2):
#     print(i ,'is a odd number')

# for a in range(2,21,2):
#     print(a,'is a even number')

# s=''
# for i in range(1,20):
#     s+=s
#     if i %2 ==0:
#         print(i,'is a even nummber')
#     else:
#         print(i,'is a odd number')

# 1. Even or Odd

# Write a Python program that asks the user for a number and checks whether it is even or odd.

# a=int(input('enter the number :'))
# if a%2==0:
#     print(a,'is the even number')
# else:
#     print(f'{a} is the odd number')

#  2. Age Group
# age=int(input('enter the number :'))
# if age <= 13:
#     print('child')
# elif age>=13 and age<=19:
#     print('teenager')
# elif age>=20 and age<=59:
#     print('adult')
# else:
#     print( 'senior')
# Take input for a person’s age and print:

# "Child" if age < 13

# "Teenager" if age is between 13 and 19

# "Adult" if age is between 20 and 59

# "Senior" if age is 60 or above

# 3. Maximum of Three Numbers

# Write a program that takes three numbers as input and prints which one is the largest.
# a=int(input('enter the number :'))
# b=int(input('enter the number :'))
# c=int(input('enter the number :'))
# if (a>b and a>c) :
#     print(a,'is the largest number')
# elif (b>a and b>c):
#     print(b,'is the largest number')
# else:
#     print(c,'is the largest number')
# # 4. Grade Calculator

# Input a student’s marks (0–100) and assign grades:

# 90–100 → "A"

# 75–89 → "B"

# 50–74 → "C"

# Below 50 → "Fail"

# 5. Leap Year Checker

# Write a program to check if a given year is a leap year or not.
# (Hint: A year is a leap year if it is divisible by 400, or divisible by 4 but not by 100.)

# Do you want me to also write the Python code solutions for these, or just keep them as practice questions?
# a=int(input('enter a number :'))
# if (a%400==0) or (a%4==0 and a %100 !=0):
#     print(a,'is the leaf year')
# else:
#     print(a,'is not leaf year')
# I prefer this response

# year = int(input('enter the year :'))
# if year%400 == 0:
#     print(year,'it is a leaf year')
# elif year%100 ==0:
#     print(year,'it is not leaf year')
# elif year%4 ==0:
#     print(year,'it is a leaf year')
# else:
#     print(year,'is not a leaf year')