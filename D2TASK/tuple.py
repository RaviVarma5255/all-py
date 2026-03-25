# What is a Tuple in Python?
# A tuple is:

# An ordered collection of items

# Immutable (you cannot change, add, or remove elements after it's created)

# Can hold items of different types

# Often used for fixed collections of values

# tp=(1,2,3,4)
# print(len(tp))
#tuple kii () evi pettali don't remember it ...

#Elements are ordered
#Elements can be of different types
#Tuples can contain duplicates

# tp1=("ravi","varma","siva","subba")
# print(len(tp1))
#gutu pettu ko royi () evvi use cheyali...
#same as list.. but add cheyadaniki vundahu exmaple

#tp2=("ravi","varma","lokesh","mart")
#tp2[2]=("mahesh")
#print(tp2)

# tp3=("mon","tus","wed","thur")
# tp3=tp3+("fri","sat","sun")
# print(tp3)
#ila cheeysukovali , i mean tuple ki add cheyali antey + operator use cheystamu..

# tp4=("bajji","idly","puri","sambar","vada")
# print(tp4[2])
# gutu pettukovalisina visayam enti antey index kii [] ivey use cheyali..

# tp6=("msdhoni","cricket","chennai")
# print(tp6[-1])
#ikkada emi cheysamu antey minus lo ichamu , thaat means rigth to left op vastadi..

# tp7=("outline","timeline","python")
# print(str(tp7[-1])[0])
#ikkada emi cheysamu antey R2L nuchi 0 index oka element nii print cheylai antey ila cheyali..

# tp5=(1,2,4,8,9,"varma","siva")
# print(len(tp5))
#length eppudu 1 nuchi start avutadi..

# t=("appel","banana")
# new_t=t + ("cherry",)
# print(new_t) #why we should put cooma ,:-tuples r immutable ,python , ikkavakpotey string laga tesukuntadi ...tuple kinda tisukodu..


# a=(1,2,3)
# b=list(a)
# b.append(4)
# a=tuple(b)
# print(a)


# k=[1,2,3,5,6,7]
# k[2]=k[2]+6
# print(k)

# a=(1,2,3,4)
# for i in a:
    # if i%2==0:
    #  print('hr',i)


a = [10, 20, 4, 45, 99, 99, 67]

first = second = -999999  # very small number

for num in a:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second highest:", second)
