# even r odd in if and while and function and lambda

# a=int(input('enter the number :'))
# if a%2!=0:
#     print('odd number')
# else:
#     print('even number')


# a=int(input('enter the number :'))
# b=0
# while a>0:
#     b=+2
#     break
# if a%2!=0:
#     print('odd number')
# else:
#     print('even number')
   

# Level 1 (Warm-up)

# Given a number, check if it is prime.
# a=int(input('enter a num :'))
# prime ki condition enti antey divisible by 1 tho avali alagey itself is called prime number
# b=0
# for i in range(1,a+1):
#     if a%i==0:
#         b+=1

# if b==2:
#     print('it is a prime number')
# else:
#     print('it is not a prime')

#     d=c
#     d=b
# if d==c and d==b:
#     print('it is a prime number')
# else:
#     print('it is not a prime number')

# Print factorial of a number (using loop).
# a=int(input('enter a number :'))
# re=1
# for i in range(1,a+1):
#     re = re*i
# print(f'factorial of {a} is {re}')


# ipppudu nenu ikkada 4 enrey cheysanu so re anedi 1 undi ok next loop loki ra range start 1 nuchi and a+1 antey input lo 5 istey 5 dakka tisukuntadi enduku antey antey adi
#  dakka tisukuntadi

# Print the sum of digits of a number.

# a=int(input('enter a num :'))
# s=0
# for i in str(a):
#     s+=int(i)
# print(s)


# while loop  without using int and str

# Reverse a number (without slicing).

# a=[1,2,3]
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# Level 2 (Bit harder)

# Check if a number is Armstrong number (e.g., 153 = 1³+5³+3³).

# Find the GCD (Greatest Common Divisor) of two numbers.

# Print all prime numbers between 1 and N.

# Print Fibonacci series up to N terms.

# Level 3 (Hard ones 🚀)

# Given a number, check if it is a Neon number (e.g., 9 → 9²=81 → 8+1=9 ✅).

# Check if a number is a Strong number (sum of factorial of digits = number).

# Print all Palindromic numbers between 1 and 500.

# Find the second largest number in a list without using max() or sorted().

# a=int(input('enter a number :'))
# # b=str(a) /naku digit to digit kavali kabathi str(a) ani tisukuna
# s=0
# for i in b:
#     s+=int(i)**3 ikkada i print cheystey 1 oka sari vastai 5 oka sari vastai alagey 3 oka sari vastadi
# daniki i mean 1 ki +1 algey **3 cheystadi 
# if s==a:
#     print('arm strong')
# else:
#     print('not arm')


# <<<<<<< while loop loo >>>>>>>>>>>
# a=int(input('enter a number :'))
# b=0
# while True:
#     for i in range(1,a+1):
#         if a%i==0:
#             b+=1
#     if b==2:
#         print('prime')
#         break
#     else:
#         print('not prime')
#         break
        
# <<<<<<<<<<functions lo elano chudam>>>>>>>>>
# def a(b):
#     c=0

#     for i in range(1,b+1):
#         if b%i==0:
#             c+=1
#     if c==2:
#         print('prime')
#     else:
#         print('not prime')
# a(3)
# a(24)
# a(103232)
# a(5)
# a(6)

# prime 
# a=int(input('enter the number :'))
# b=0
# for i in range(1,a+1):
#     if a%i==0:
#      b+=1
# if b==2:
#     print('prime')
# else:
    # print('not prime')

# factorial
# a=int(input('enter the number :'))
# b=1
# for i in range(1,a+1):
#     b*=i
# print(b)

# neon number 
# a=int(input('enter a number :'))
# b=a**2
# c=0
# for i in str(b):
#     c+= int(c)
#     print(i)

# if c==a:
#     print('neon')
# else:
#     print('not neon')

# Arm strong
# a=int(input('enter the num :'))
# b=str(a)
# s=0
# for i in b:
#     s+=int(i)**3
# print(s)
# if s==a:
#     print('arm strong')
# else:
#     print('not arm strong')

# for i in range(6,1,-1):
#     print(i)



# # Create a class Vehicle:
#     # Attributes: brand, model
#     # Method: show_vehicle_info(

# class vehicle:

#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#         print(f'{self.brand} is the {self.model}')

# # Create a class SmartDevice:
#     # Attributes: device_name, version
#     # Method: show_device_info()

# class smartdevice:
#     def show_device_info(self,name,version,brand,model):
#         super().__init__(self,brand,model)
#         self.name=name
#         self.version=version

# # Create a class SmartCar that inherits from both Vehicle and SmartDevice:
#     # Adds attribute: connectivity (e.g., "5G", "Wi-Fi")
#     # Method: show_full_info():
#     # Should print brand, model, device name, version, and connectivity

# class smartcar(vehicle,smartdevice):
#     def show_full_info(self,brand,model,name,version,connectivity):
#         super().__init__(self,brand,model,name,version)
#         self.connectivity=connectivity

# ob=smartcar('bmw','200cc')
# ob.show_full_info('bmw','200cc','siva','reloaded','wi-fi')
# # print(ob.show_full_info)
        

# a=int(input('enter a number :'))
# b=str(a)
# c=0
# for i in b:
#     c+=int(i)**3
# print(c)
# if c==a:
#     print('arm strong number')
# else:
    # print('not arm strong'


# for i in range(100,1001):
#     a=len(str(i))
#     b=0
#     for s in str(i):
#         b+=int(s)**a
#         # print(b)
#     if b==i:
#         print(i)


# a=['varma']
# for i in a:
#     for v in i:
#         print(v)

# b=['ravi']
# for k in b:
#     print(k)
#     for j in k:
#         print(j,ord(j))


# iddi for loop 
# l=[1,2,3,4,5,6,8]
# even=[]
# odd=[]
# count=0
# sum=0
# c=0
# s=0
# for i in l:
#     if i%2==0:
#         sum=i+sum
#         count+=1 #count kii 
#         even.append(i)
#     elif i%2!=0:
#         odd.append(i)
#         s=i+s
#         c+=1
# print(odd,'odd numbers')
# print(s,'is the total sum of odd')
# print(c,'is the count of odd')
# print(even,'even numbers')
# print(sum ,'is the total sum of even')
# print(count,'is the even count in list')


# h=[5,6,7,8]
# for g in h:
#     if g!=8:
#         h.append(9)
#         print(h)
        
#     else:
#         print('ok')


# k=['varma','ravi']
# for ki in k:
#     for j in ki:
#         if j=='a':
#             print(7,ki)

        






