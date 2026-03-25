# usk
# 
# ltack development')
# else:
#     print('go and learn skills')


# acc=int(input('enter your amount:'))
# acc_bal=30000
# if(acc_bal<acc):
#     print('insufficient balance')
# elif(acc_bal>=acc):
#     print('please wait while transaction is processing')
#     if(acc%100==0):
#         print('trasaction done please collect the amount')
#     else:
#         print('withdrwal amut should be multiples of 100 only')

#1.even amd odd using input
# a=int(input('enter a num:'))
# if(a%2==0):
#     print('num is even')
# else:
#     print('num is odd')

#2.Divisible by 5 but Not by 10
# b=int(input('enter a number:'))
# if(b%5==0 and b%10!=0):
#     print('Satisfy')
# else:
#     print('not satisfy')

#3.Biggest Among Two Numbers
# a=int(input("a:"))
# b=int(input('b:'))
# if(a>b): #ikkada condition wrong ichamu boc else print avadaniki..
#     print('biggest is')
# else:
#     print('biggest is:',b) #ila kuda cheyachu..

#4.smallest among two numbers
# c=int(input('c:'))
# d=int(input('d:'))
# if(c<d):
#     print('smallest is',c)
# else:
#     print('samllest is:',d )

#5.Divisible by 2, 3, and 6

# d=int(input('number:'))
# if(d%2==0 and d%3==0 and d%6==0):
#     print('satisfy')
# else:
#     print('unsatisfy')

#6.Voting Eligibility
# a=int(input('Enter age:'))
# age=18
# if(age>=18):
#     print("Eligible to vote")
# else:
#     print('wait until ur trun to 18 or more to vote')

#7.Student Pass/Fail Based on All Subjects >= 35
#Question: Check if a student passed all subjects (maths, physics, chemistry). 
# #Explanation: Student passes only if marks in all subjects are 35 or more. - 
# Input: Maths = 40, Physics = 36, Chemistry = 30 - Output: Fail

# a=int(input('enter maths marks:'))
# b=int(input('enter physics marks:'))
# c=int(input('enter chemistry marks:'))
# if(a>=35 and b>=35 and c>=35):
#     print('pass')
# else:
#     print('fail')

#8.Student Pass if Passed Any One Subject (>= 35)
#Question: Check if the student passed at least one subject. 
# Explanation: Use logical OR to check if any one subject has marks >= 35. - 
# Input: Maths = 20, Physics = 38, Chemistry = 25 - Output: Pass

# mat=int(input('enter maths marks:'))
# phy=int(input('enter physics marks:'))
# che=int(input('enter chemistry marks:'))
# if(mat>=35 or phy>=35 or che>=35):
#     print('pass')
# else:
    # print('fail')

#9.9. Student Pass if Passed Any Two Subjects
#Question: Check if the student passed any two out of three subjects. 
# Explanation: Use a counter or logical conditions to verify two subjects >= 35.  
# Input: Maths = 40, Physics = 20, Chemistry = 36 - Output: Pass

# m=int(input('enter maths marks='))
# p=int(input('enter physics marks='))
# c=int(input('enter chemistry marks='))
# if(m>=35 or p>=35) and (c>=35 or m>=35)  :
#     # if(c>=35 or m>=35):
#     print("pass")
# else:
#     print('fail')

# 10.Biggest Among Three Numbers
# Question: Find the biggest number among three.
# Explanation: Compare each pair of numbers using 
# if-else conditions. - Input: A = 7, B = 4, C = 9 - Output: Biggest is: 9

# a=int(input('A='))
# b=int(input('B='))
# c=int(input('C='))
# if(a>b and a>c):
#     print(f'biggest is {a}')
# elif(b>a and b>c):
#     print(f'biggest is {b}')
# else:
#     print(f'biggest is {c}')

#11. Smallest Among Three Numbers
#Question: Find the smallest number among three. Explanation: 
#Use comparison logic to determine the minimum value. - Input: A = 7, B = 4, C = 9 - Output: Smallest is: 4

# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))

# smallest=min(a,b,c)
# print(f'smallest is {smallest}')
# ila kakunda 
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# if(a<b and c<a):
#     print('smallest is ',a)
# elif b<a and b<c:
#     print("samllest is",b)
# else:
#     print('smallest is ',c)

#12.<<<<< Perfect Square or Not
#Question: Check if a number is a perfect square.
# Explanation: A number is a perfect square if the square of its square root equals the number.
#  - Input: Number = 49 - Output: Perfect square >>>>>
# v=int(input('enter the num='))
# sq_root=v**0.5
# if(sq_root*sq_root==v):
#     print('is perfect square')
# else:
#     print('is not perfect square')

#13. Cars Required for Members (Max 5 per car)
# Question: Calculate how many cars are needed for a given number of people. 
# Explanation: Divide total people by 5 and round up using ceiling logic. - 
# Input: Members = 17 - Output: Cars needed = 4

# u=int(input('enter the num:'))
# if(u//5==0):
#     print(f'{u} max 5 mems for car') 
# else:
#     print(f'{(u//5)+1} cars are req') #input lo u=49 tisukuntam kabbati u//5 ichamu so 45/5=9 so for another 
    #4 mems i want i can that y 10 is printed..

# 14. Second Biggest Among Three Numbers
# Question: Find the second largest number among three inputs. 
# Explanation: Use sorting or nested conditions to find the second largest value. - 
# Input: A = 10, B = 25, C = 18 - Output: Second biggest: 18

# q=int(input('enter a num='))
# w=int(input('enter the num='))
# e=int(input('enter the num='))
# if(q>w and w<e) or (q<w and e>w):
#     print(f' 2nd biggest  is{q}')
# elif(w<e and q<e) or (e<w and e>q):
#     print(f' 2nd biggest is{w}')
# else:
#     print(f' 2nd biggest is{e}')

# # def add(*a):
#     print(sum(a))
# add(1,2,24,45,5,6,65,9)

# def perpare_a_tea(*a):
#     print('on the stove')
#     print('put the bowl in stove')
#     print('add water & milk')
#     print('and tea powder')
#     print('serve the tea')
#     print(a)
# perpare_a_tea('how was the taste?')

# perpare_a_tea('too good')

# def ravi():
#     print('hello')
#     return ('hi')
# print(ravi())

# def add(a, b):
#     return a + b

# result = add(4, 5)
# print(result)

# def ravi(a,b):
#     print(a+b)
# ravi(100,400)


# def varma(a,b,c):
#     return a+b-c
# ravi= varma(4,6,1)
# print(ravi)
# y=varma(2,2,2)
# k=varma(4,5,1)
# print(k)
# print(y)

# def sub(a,b):
#     print(a-b)
#     return a
# sub(5,3)

# a=[1,2,(8,2,3),8,2,6,5]
# b=a[2][0]**2
# print(b)

# list=[1,2,3]
# list.add(7,8,'hii')
# print(list)

# for a in range(1,20):
#     if a==5:
#         break
#     print(a)

# a='ravivarma'
# for s in a:
#     if s==(a[3]):
#         break
#     print(s)

# b="user"
# for w in b:
#     if w==(b[1]):
#         break
    # print(w)
# else:
#     print('code work avutudi ra mawa')

# num=list(range(1,100))
# for i in num:
#     if i>50:
#         break
#     print(i)

# num=list(range(1,100))
# for i in num:
#     if i==50:
#      continue
#     print(i)

# a='ravivarma'
# for i in a:
#    if i==a[3]:
#       continue
#    print(i)


# Problem:
# Write a program that takes a number and prints whether it's positive, negative, or zero.

# num = float(input("Enter a number: "))
# if num>0:
#     print('postive')
# elif num<0:
#     print('negative')
# else:
#     print('zero')

# Grading System
# Take marks (0 to 100) as input and print the corresponding grade:

# 90–100: A

# 80–89: B

# 70–79: C

# 60–69: D

# Below 60: F 

# a=int(input('enter the number='))
# if a>=90 and a<=100:
#     print('A')
# elif a>=80 and a<=89:
#     print('B')
# elif a>=70 and a<=79:
#     print('C')
# elif a>=60 and a<=69:
#     print('D')
# elif a<=60:
#     print('F')
# else:
#     print('plz enter the valid num')

# Check if a number is divisible by 5 and 11.

# a=int(input('enter the number:'))
# if a%5==0 and a%11==0:
#     print(f'{a} is divisilbe by 5 and 11')
# else:
#     print('enter a valid number')

# Find the largest of two numbers
# a=int(input('enter the number of a:'))
# b=int(input('enter the number of b:'))
# if a>b:
#     print(f'{a} is the largest number')
# elif a<b:
#     print(f'{b} is the largest number')
# else:
#     print('both are equal numbers')

# Check if a year is a leap year
# year = int(input('enter a year:-'))
# if (year%4==0 and year%100!=0 or year%400==0):
#      print(f'{year} is leap year')
# else:
#     print('not leap year')

# Check if a character is a vowel or consonant
# ch = input("Enter a single character: ")
# a='aeiouAEIOU'
# if ch in a:
#     print('vowels')
# elif ch.isalpha():
#     print('consonant') 
# else:
#     print('plz enter valid character')

# Find the largest among three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a>b and a>c:
#     print(f'larhest among three is {a}')
# elif b>a and b>c:
#     print(f'larhest among three is {b}')
# elif c>a and c>b:
#     print(f'larhest among three is {c}')
# else:
#     print('dont give eqaul numbers')

# 
# print second largest num
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a>b and a<c:
#     print(f'second is {a}')
# elif b>a and b<c:
#     print(f'second is {b}')
# elif c>a and c<b:
#     print(f'scond is {c}')
# else:
#     print('motma')

# Triangle Type
# Input the lengths of three sides of a triangle and determine whether the triangle is equilateral, isosceles, or scalene.

# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# c=int(input('enter the number:'))
# if a + b > c and a + c > b and b + c > a:
#    if a==b==c:
#     print('it is a Equilateral')
#    elif a==b or b==c or c==a:
#     print('it is a Isosceles')
#    else:
#     print('it is Scalene')
# else:
#   print('it is not a vaild triangle')

#  1. Largest of Three Numbers with a Twist
# Take three numbers from the user.

# Print the largest,

# But also print "All are equal" if they’re the same.

# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# c=int(input('enter the number:'))
# if a>b>c:
#     print(f'{a} is the largest')
# elif b>a>c:
#     print(f'{b} is the largest')
# elif a==b and b==c:
#     print('All are equal')
# else:
#     print(f'{c} is the largest')

# 2. Evenly Divisible Checker
# Take two numbers as input.
# Check if the first is divisible by the second.
# If not, print how much remainder is left.
# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# if a==0 and b==0:
#     print('divisionable of zero is not allowed')
# elif a%b==0:
#     print(f'{a} is divisible by the {b}')
# else: 
#     print(f'{a%b} is the remainder')

# 3. Marks to Grade with Validity Check
# Input marks (0–100).
# If marks are invalid (<0 or >100), print "Invalid Marks".
# Otherwise, assign grades

# a=int(input('enter the number='))
# if a>=91:
#     print('A grade')
# elif a>=81:
#     print('B grade')
# elif a>=71:
#     print('C grade')
# elif a>=61:
#     print('D grade')
# elif a>=51:
#     print('E grade')
# elif a>=10:
#     print('F fail')
# elif a<=0 or a>=100:
    # print('Invalid marks')

# # Input: marks
# marks = float(input("Enter your marks: "))

# # Check for validity
# if marks < 0 or marks > 100:
#     print("Invalid Marks")
# else:
#     # Assign grades based on marks
#     if marks >= 90:
#         print("Grade: A")
#     elif marks >= 80:
#         print("Grade: B")
#     elif marks >= 70:
#         print("Grade: C")
#     elif marks >= 60:
#         print("Grade: D")
#     else:
#         print("Grade: F")

# 4. Login System
# Ask for a username and password.
# If username is "admin" and password is "1234", print "Login successful"
# Else, print "Invalid credentials"
# username=(input('enter username:')) 
# password=int(input('enter password=')) 
# if username=='admin'and password==1234:
#     print('login successful')
# else:
#     print('Invalid credentials')

# 5. Quadratic Root Type Checker
# Given three coefficients a, b, and c, calculate the discriminant:
# D = b² - 4ac
# If D > 0 → "Real and Distinct"
# If D == 0 → "Real and Equal"
# If D < 0 → "Complex Roots"
# a=int(input('enter a number:'))
# b=int(input('enter a number:'))
# c=int(input('enter a number:'))
# D= b ** 2 - 4*a*c
# if D>0:
#     print('Real and Distinct')
# elif D == 0:
#     print('real and eqaul')
# else:
#     print( 'Complex Roots')

# 6. Odd or Even Digit Count in a Number
# Input a number, and count how many even and odd digits it has.
# (E.g., for 1243 → Even: 2, Odd: 2)

# a=4
# count=0
# if a%2==0:
#     print(f'{a} is even numb')
#     count+=1
#     print(count)
# else:
#     print(f'{a} is odd num')

# 7. Bill Discount System
# Input the total amount:
# If total ≥ 1000 → 20% discount
# If total ≥ 500 → 10% discount
# Else → No discount
# Print final amount after discount.

# a=int(input('enter the number='))
# b=a*0.20
# c=a*0.10
# if a>=1000: 
#     print('20% discount')
#     fin_amo=a-b
# elif a>=500:
#     print('10% discount')
#     fin_amo=a-c
# else:
#     print('no discount')
# print(f' final amount is {fin_amo}')

# discount = amount * (discount_percent / 100)
# final_amount = amount - discount 

#  1. Maximum of Three Numbers
# Problem:
# Input three numbers from the user. Print the largest one using only if, elif, and else (no max() or sorting).

# Example Input: a = 10, b = 25, c = 15
# Expected Output: Maximum is 25
# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# c=int(input('enter the number:'))
# # Python interprets it as:(a > b) and (b > c)
# if a>b>c or a>c>b:
#     print(f'largest number is {a}')
# elif b>a>c or b>c>a:
#      print(f'largest number is {b}')
# else:
#       print(f'largest number is {c}')
# Test 1: a > b > c
# Breaks down as:
# a > b → 2 > 3 → ❌ False
# b > c → 3 > 4 → ❌ False
# Final Result: False
# Test 2: a > c > b
# Breaks down as:
# a > c → 2 > 4 → ❌ False
# c > b → 4 > 3 → ✅ True
# But since both must be true, final result: False

# Problem:
# Input a 3-digit number and check whether it is an Armstrong number or not.
# A number is Armstrong if:  abc=a**3+b**3+c**3
# Example Input: 153
#Expected Output: Armstrong number
#Because: 1**3+5**3+3**3=153..

# num = int(input("Enter a 3-digit number: "))

# # Extract individual digits
# a = num // 100           # Hundreds place
# b = (num // 10) % 10     # Tens place
# c = num % 10             # Units place

# # Calculate sum of cubes
# s = a**3 + b**3 + c**3

# # Armstrong check
# if s == num:
#     print("It is an Armstrong number")
# else:
#     print("It is not an Armstrong number")

# print(f"{s} is the sum of cubes of its digits")

#using foor loop

# a=int(input('enter the number='))
# for x in range(a,a+1):
#     if :
#         print('it is armstrong number')


# 1.wap check given number present in collection or not
# a=[1,2,3,4,5,573,72728]
# b=int(input('check given number present in collection='))
# if b in a:
#     print('present')
# else:
#     print('not present')

# 2.wap username password valid or not 
# username='ravi'
# password=1234
# if username == 'ravi' and password==1234:
#     print('valid')
# else:
#     print('not valid')

# 3.wap take a single string check that string is lowercase or not if it is lowercase print that string next character
# a=input('enter a str:')
# if "ravi" in a and len(a) > 1:
#     print(" it is lowercase ,Next character is:", a[1])
# elif 'RAVIVARMA' in a:
#     print("It is not lowercase.")
# else:
#     print("It is not lowercase or too short.")





