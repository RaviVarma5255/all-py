# What is a Set in Python?
# A set is:
# 1 An unordered collection of unique items.
# 2 Mutable (you can add/remove items).
# 3 Doesn't allow duplicate values.
# 4 it will be denoted by {} ..

# a1set={"ravi","varma","sai","cs","chandu","ram"}
# print(a1set)
#set annadi unordered kabbti 1st ravi , 2nd varma ila print avkunda , dani unique way loo output istadi..
#soo 1st point justified..

#number 2 
#sets r mutable antey change chesukovachu anni ardham..
#ex:-
# a2set={22,5,7,9}
# a2set.add(38)
# print(a2set)
#indullo manamu 38 anney num add cheysamu..
#mutilpe nums add cheyali antey update aney method use cheyali..

# #ippudu string kii adding chudam..
# a3={"ravi","rp","cs","sai","chandu",}
# a3.add("varma")
# print(a3)
#soo ikkada varma an ey string add avutadi but a3 ichina oder lo undadhu coz of sets r unordered..

# a4={"tv","house","bike","phone"}
# a4.remove("tv")
# print(a4)
#ikkada remove method use cheysamu , just niku emi remove cheyli anukutunavo addi remove()anni peditey chalu..
#soo point num 2 justified..

#point num3 :-
#sets annadi duplicate values nii print cheyadhu..
#ela noo chudam..
# a5={1,2,3,4,5,6,1,2,3,4,5,6}
# print(a5)
#{1, 2, 3, 4, 5, 6} naku vachina op iddi , soo point 3 justified...

#inka unati ..


# METHODS IN SETS 

# 1 ADD : just oka element ney add cheyadaniki untadi
# a={'ravi','siva','mahi'}
# a.add('varma')
# print(a)

# 2 REMOVE : USED TO REMOVE SPECIFIC ELEMENT IN A SET
# b={'varma','btech','batting'}
# b.remove('btech')
# print(b)

# 3 POP () : IT IS USED TO POP ONE ELEMENT IN A SET
# c={'phone','laptop','games'}
# c.pop()
# print(c) evo redu mataramey print avutai

# indulo inko method chudam
# z={1,3,5,6}
# v=z.pop()
# print(v)

# 4 COPY() : it is used for  copy a set into another set
# d={'ravi','siva'}
# e= d.copy()
# print(e)

# 5 CLEAR : IT IS USED TO CLEAR ALL THE DATA IN THE seT
# f={'siva','subba','dantuluri'}
# f.clear()
# print(f) op : - set ()

# 6 UPDATE : IT IS USED TO ADD 1 R MORE ELEMENTS IN THE SET 
# g={'good','nerchuko','ok na'}
# h={'alagey','nerchukuntha'}
# # g.update(h)
# h.update(g)
# print(h)  ila kuda ivachu 
# print(g)

# ippudu  INKO 3 METHODS ADD CHEYDAM vitiiki o/p boolean type lo vastai
#1 ISDISJOINT 2 ISSUBSET 3 ISSUPERSET 
# 1 ISDISJOINT : set1 and set 2 has unique values then only the op will be true otherwisse it will be false
# a={'ravi','varma'}
# b={'siva','ravi'}
# c=a.isdisjoint(b)
# print(c) op false

#  for true
# a={1,2,3,4}
# b={5,6,7,8,9}
# z=a.isdisjoint(b)
# print(z)

# 2 ISUBSET() : SET1 LO VALUES ANNI SET 2 LO UNDALI APPUDUEY TRUE VASTDI <= is the symbol for this
# s={1,2,3,4}
# v={4,5,6,7,12,3,1,2}
# p=s.issubset(v)
# print(p)

# for false :
# m={1,2,3,4}
# n={1,3,4,5,6}
# o = m.issubset(n)
# print(o) op false

# 3 ISSUPERST() SET 2 LO UNNA VALUES ANNI SET 1 LO UNTEY TRUE VASTADHI
# r={1,2,3,4,5,9}
# p={2,3,4,1,5,8}
# x=p.issuperset(r)
# print(x)

# ee methods saripotai
# add
# clear
# remove
# pop 
# copy 
# update

# ivvi kadhu da 

# discard : it is used to remove specific element in the set 
# main ga remove ki discard ki diff anti antey 
# remove > throws error if x not present
# discard > ignores if x not present iddi error rasie cheyadhu
# a={1,2,3,4}
# a.discard(2)
# print(a)


# intersection : rendu sets lo a values ayitey untao avey return cheyastadhi
# a={1,3,4}
# b={2,5,4}
# v=a.intersection(b)  ila mention cheysukovali
# print(v)


# union : it is combie both the sets and return in one set of values

# v={1,2,3,5}
# b={2,3,4,5,6,7,'siva'}
# c=b.union(v)
# print(c)


# difference : it is usede to identified the  diff elements in the both sets 
# set1={3,4,5,6}
# set2={2,7,89,4,6}
# v=set2.difference(set1)
# print(v)

# difference_update :
a={1,3,4,6}
b={4,5,6,78}
a.difference_update(b)
print(a)

# ivvi kakuda 
# isdisjoint
# issubset
# issuperset
