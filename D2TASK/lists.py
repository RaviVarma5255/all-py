# What is a List in Python?
# A list is:

# An ordered collection of items

# Mutable (you can change, add, or remove elements)

# Can hold items of any type (integers, strings, even other lists)

x=[1,2,3,4,5,6,7,8]
print(len(x))
#length of the list , we see here i give 8 nums so op will be 8

x=["family","members","friends","tasks"]
print(len(x))
#indulo strings oka length chusam , op:- 4
#ee pyna rendhu lists homogeneous.....

a=[1,2,3,5,7,"laptop","mouse","keyboard"]
print(len(a)) #op:-8

b=["hello","coders","python",78,91,0]
print(len(b)) #op :-6

#ee pyna rendhu heterogeneous....

c=["ab","bc","cd","de","ef"]
print(c[2]) #op:-cd
#index kii [] ee brackets ivali

d=[1,98,79,56,673,90]
print(d[5]) #op:-90
#ee pyna c&d laa kii index check cheysam , postive values lo left to right side kii , alagey index left to right kii 0 nuchi start avutadi

e=["book","bags","rooms","classes","roads"]
print(e[3][0]) #op:-c
#indulo emi cheysamu antey list lo unna edo oka index nii tesukuni andulo first index print cheysamu

f = [2, 9, 0, 458, 99, 898, 32]
op =str(f[3])[2]   # This gets the third digit of 458
print(op)           # Output: '8' (as a string)
#brackests mataram baga chueukovali , akkada op daggra str(f[3])[2] ila isteney op print avutadi...lekkapote error vastadi

g=[3,6,5,9,0]
print(g[-1])
#brackets mattarm mari mari chusukovali , indulo right to left index chusam , negative loo

h=["varma","raju","baby"]
print(h[-2])
#ikkada -2 ichamu kabbati adi right to left tesukuntadi, so manaki raju op vastadhi..

i=[37,3728,728,977,938]
print(str(i[-1])[-1])
#ikkada chusukuntey right num 938 tisukunam indulo 2 index adigitey 8 vachindi..

j=["devi","satya","pranathi","b raju"]
print(j[-3][0])
#ikkada emi cheysamu antey right to left kii negative lo print cheysamu , R2L ki index -1,-2,-3.. ila vastadhi

k=[1,2,3,5,6,7]
k[2]=k[2]+6
print(k)
#increment.. ,deniki anni variables same iavli

l=["hello","bye"]
kp=l+[5]
print(kp)

o=["siva","subba","ravi","varma"]
o=o+["rama","krishna","raju"]
print(o)

list=["mon","tues","wed","sat"]
list=list+["sun"]
print(list)

#ikkada emi cheysamu antey list kii inko element add cheysamu ,daniki + use cheysamu
#ika untey delete anni pop anni unatyi & remove kudha untadi...

n=["hi","hello","welcome"]
n[2]="bye"
print(n) #idi updated list...
#indulo add cheysukovachu, i mean n aney list loo welcome place loo bye print cheyali , antey n[2] = bye anni peditey op vastadi..

m=[1,2,3,4,5,"ravi","varma"]
print(m[2:7]) #ikada chusunatu undi antey ,ikkadey length & index same oka dagarey print avutadi..
#2 index antey 3 nuchi 7 icha kabbati last dakka output vastadhi..

#SLICEING METHOD ...(start:end:step)
#step eppudu -1 defalut, start 0 tho avutadi , end kii.... soo -2 antey -1 ani ardam , -3 antey -2 anni ardam 
#ending kii eppudu oka index mundidey tisukovali.. 

# a=[1,2,3,4,5,6,7,8]
# a=a[4:3:-1] # iddi slice method , [:::] 1st dii start, 2nd dii end, 3rd dii step or skip
# print(a) #ikkada inkotai observe cheyalisina dii enti antey sarting index pedda dii ivali & end dii -1 ivali , i mean 6-1=5 ila & last dii -1 ichamu. 
# #indulo emi cheysamu antey , nenu only 5 okatey print cheyali anukuna adi kuda slice loo 

# b=[1,2,3,4,5,6,7,8,9]
# b=b[0:2]+b[7:9]
# print(b) #staring 2 nums & last 2 nums ila add cheysukovachu.. ee code ki op:-[1, 2, 8, 9] 

# v=[33,4,11,32,90,82,2,43,78]
# y=len(v)//2
# print(y) # ila istey list oka len nii tisukuni by cheysamu.. op:-4..

# y=[40,29,81,43,26,54,25]
# x=len(y)//2
# print(y[x:]) # len of the whole list divide by 2 and staring lo x ichamu kabbati 2nd half print ayyindi..

#1st half print avali antey 
# z=[21,22,22,24,25,26,27,28]
# w=len(z)//2
# print(z[:w])  # op-[21, 22, 22, 24] ila yenduku vachindi antey start lo emi ivley kabbati adi default ga tesukuntadi..
 



 #date 29
# l=[1,4,6,8,4,7]
# y=l.index(8)
# print(y)

# u=[1,4,5,6,8,9,5,3,2]
# print(u[2])

# p=["ravi","fans","lists","remove"]
# p.pop(2)
# print(p)

# k=[731,4322,482857,272,7520,892]
# k.append(843)
# print(k)

# p=[729752,"rabi","euefq","gwygfwg"]
# p.reverse()
# print(p)

# m=["qhf","ihu","houwhw","hih",2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# y=m.count(h)
# print(y)




