# print('*')
# print('**')
# print('*'*7)
# print('*'*2 +'*')
# print('*'*9 +'****')
# for i in range(0,5):
     
#     print('*')
# ila istey column ga oka oka star vastadi

# for i in range(5):
#     print('*',end='')
#  ***** ila vastadhi 

# for a in range(0,4):
#     print(' ')
#     for b in range(0,1):
#         print('*')


# a=''
# for b in range(1,5):
#     a+='*'
#     print(a)
# At a=0 → adds 1 star
# At a=1 → keeps old star + adds 1 more
# At a=2 → keeps 2 stars + adds 1 more
# At a=3 → keeps 3 stars + adds 1 more

# b=''
# for a in range(5):
#     b+='*'
#     print(b)
# Step by step:
# a=0 → b = "*" → prints *
# a=1 → b = "**" → prints **
# a=2 → b = "***" → prints ***
# a=3 → b = "****" → prints ****
# a=4 → b = "*****" → prints *****

# b=''
# for a in range(5):
#     b+='*'
# print(b)
# Step by step:
# After loop ends, b = "*****"
# Only one print happens

# for a in range(5):
#     b=''
#     b+='*'
#     print(b)
# Step by step:
# Every loop resets b → "*"
# Prints "*" each time

# for a in range(5):
#     b=''
#     b+='*'
# print(b)
# Step by step:
# Each loop sets b = "*" but never prints inside loop
# After loop ends, b is still "*"
# Prints only "*"

# for a in range(4):
#     # b=''
#     # b+='ravi'
#     print('ravi')

# a=''
# for b in range(4):
#     a+='ravi'
#     print(a)

# for b in range(4):
#     a=""
#     a+='ravi'
# print(a)

for a in range(5):
    print('varma')
    if a==0:
        print('hello')
    elif a==3:
        print('ravi')
    elif a==4:
        print('going good')
