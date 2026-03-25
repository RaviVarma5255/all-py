# # class A:
# #     a=20 #ivvi class variables
# #     b='ravi' #ivvi class variables

# #     def __init__(self):
# #         self.name='varma' #ivvi instance variables
# #         self.age=22 #ivvi instance variables

# #     @classmethod

# #     def hello(cls):
      
# #       print(f'{cls.a}')

# #     @staticmethod

# #     def greet():
# #        print('hello')


# # c=A()
# # # print(A.b)
# # # print(c.name)
# # print(c.age)
# # c.hello()
# # c.greet()
# # print(A.a)
# # print()
        
# # list=[1,2,3,4]
# # list = list + [8,'hello','hooo']
# # print(list)

# # def a (*b):
# #     c=b
# #     print(list(c))
# # a(1,2,3,4)

# # def a (*b):
# #      print(list(b))
# # a('ravi',4,728,889,'kk',61)
        

# Common Python List Methods
# 1. append(x) — Add one item at the end
# python
# Copy
# Edit
# numbers = [1, 2, 3]
# numbers.append(4)
# print(numbers)  # [1, 2, 3, 4]
# Adds a single element to the end.

# Can also append other lists as one item:

# python
# Copy
# Edit
# numbers.append([5, 6])  # [1, 2, 3, 4, [5, 6]]
# 2. extend(iterable) — Add multiple items
# python
# Copy
# Edit
# numbers = [1, 2, 3]
# numbers.extend([4, 5])
# print(numbers)  # [1, 2, 3, 4, 5]
# Unlike append(), it unpacks the list and adds elements individually.

# 3. insert(index, value) — Add at a specific position
# python
# Copy
# Edit
# numbers = [1, 2, 4]
# numbers.insert(2, 3)  
# print(numbers)  # [1, 2, 3, 4]
# 4. remove(value) — Remove by value
# python
# Copy
# Edit
# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)  # ['apple', 'cherry']
# Removes the first occurrence of the value.

# 5. pop(index) — Remove by position (and return it)
# python
# Copy
# Edit
# fruits = ["apple", "banana", "cherry"]
# x = fruits.pop(1)
# print(x)       # banana
# print(fruits)  # ['apple', 'cherry']
# If no index is given, removes the last item.

# 6. clear() — Empty the list
# python
# Copy
# Edit
# numbers = [1, 2, 3]
# numbers.clear()
# print(numbers)  # []
# 7. index(value) — Find position of a value
# python
# Copy
# Edit
# numbers = [10, 20, 30, 20]
# print(numbers.index(20))  # 1 (first occurrence)
# 8. count(value) — Count occurrences
# python
# Copy
# Edit
# numbers = [1, 2, 2, 3, 2]
# print(numbers.count(2))  # 3
# 9. sort() — Sort in ascending order
# python
# Copy
# Edit
# numbers = [3, 1, 4, 2]
# numbers.sort()
# print(numbers)  # [1, 2, 3, 4]
# For descending order:

# python
# Copy
# Edit
# numbers.sort(reverse=True)
# 10. reverse() — Reverse the list
# python
# Copy
# Edit
# numbers = [1, 2, 3]
# numbers.reverse()
# print(numbers)  # [3, 2, 1]
# 11. copy() — Make a shallow copy
# python
# Copy
# Edit
# a = [1, 2, 3]
# b = a.copy()
# b.append(4)
# print(a)  # [1, 2, 3]
# print(b)  # [1, 2, 3, 4]


#instance