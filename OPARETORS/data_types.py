# list 
# tuple
# set
# dict

# a=(1,2,3,4,1,2,3,4,)
# print(list(a))

# s = "hello"
# t = tuple(s)
# print(t)         # ('h', 'e', 'l', 'l', 'o')


# t = (10, 20, 30, 20, 40,10,20)
# print(t.index(20))        # 1
# print(t.index(20, 3))     # 3  (start searching from index 2)

# frutis=('ravi','varma','siva','subba')
# print(frutis[1])

# a=22
# b=9
# print(a-b,'days go to home')

# l=[1,2,3]
# a=0
# for i in l:
#     a+=i
# print(a)

# 1. Tuple Packing & Unpacking

#      a.Pack three fruits ("apple", "banana", "cherry") into a tuple.
#      b.Unpack them into separate variables and print each one.
# a=('apple','banana','cherry')
# b,c,d = a
# print(b,'for chandu')
# print(c , 'for cs')
# print(d,'for sai')

# 2. List Packing & Unpacking

#     a.Pack the numbers 1 to 5 into a list.
#     b.Unpack so that the first element goes into a, the last element into c, and the remaining into b using *.

# litss=[1,2,3,4,5]
# a,*b,c=litss
# print(a)
# print(b)
# print(c)

# 3. Swapping Values
    # a.Swap two variables (x=10, y=20) using unpacking in one line.
# x=10
# y=20
# x,y = y,x
# print(x,y)

# 4.Given a list of student marks [95, 88, 76, 67, 89, 92], use unpacking to separate:

# 	i.topper (first value),

# 	ii .others (middle values),

# 	iii.last_student (last value).

marks = [95, 88, 76, 67, 89, 92]
topper,*others,last_student = marks
print(topper)
print(others)
print(last_student)