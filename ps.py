# remove duplicates from a list using loop or set
# a=[1,2,2,3]
# b=[]
# for i in a:
#     if i not in b:
#       b.append(i)
# print(b)  
# <<<<<<>>>>>>
# a=[1,2,2,3]
# b=set(a)
# print(list(b))


# <<<<<<<<Patreen>>>>>>
# n=10
# for i in range(1,n+1):
#     print("* " *n)
    # if i==5:
        # break

# <<<<<<rectangle>>>>>>>>>
# n=3
# for i in range(1,n+1):
#     print("* " *(n*2))

# <<<<<<<<<right angle rectangle>>>>>>>>>
# a=4
# for v in range(1,a+1):
#     print("* " *v)

# <<<<<<<<<<<

# w=3
# for c in range(1,w+1):

#     space=" "*(w-c)
#     star="* "*c
#     print(space+star)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>
# w=5
# for c in range(w,0,-1):

#     space=" "*(w-c)
#     star="* "*c
#     print(space+star)

# # w=5
# for c in range(2,w+1):

#     space=" "*(w-c)
#     star="* "*c
#     print(space+star)


# l=[1,2,3,4,5,6,78,9]
# l.append(917)
# print(l)

# a= [1,2,3,4,5,6,7,8,9]
# print(a[0])
# print(a[4])
# print(a[2]+9)
# print(a[1]*3)
# b=a[1]+3
# print(b)
# a=a+[685]
# print(a)
# print(a[-1])
# print(a[0]+1 or a[0]+2)
# if (2 and 3) in a:
    # print([2,3])
# for i in range(8,0,-2):
#     print(a[i])

# while 2 in a:
#     print(a)
#     break

# write a pp for find the length of a string without using len function
# s='sivasubba'
# q=0
# for i in s:
#     q+=1
# print(q ,'is the len of the string')

# a = [1, 2, 3]
# b=a
# b.append(4)
# print(a)

# a = [10, 20, 30, 40, 50]
# print(a[1:4])
# a[1:4] = [99]
# print(a)

data = [1, 2, 3]
print(data + data * 2)

