#List Comprehension
# squares = [x**2 for x in range(10)]
# print("This is for List",squares)

#--------------------------------------------------------------------

#Generator Expressions
# squares_gen = (x**2 for x in range(10))
# print("This is for Generator Expressions")
# for num in squares_gen:
#     print(num)

#--------------------------------------------------------------------

#Iterators and Iteratabels

#Iterable: Any object thats can loop over eg: list, strings
#Iterator: Any object with __iter__() and __next__() methods

nums = [7,5,6,3]

it = iter(nums)
# print(it.__next__()) #--> It gives me the next value i.e 7
# print(it.__next__()) #--> It will give 5

#Creating Own Interator
#Like we are creating to print 10 valuse from1 to 10

# class TopTen:
#     def __init__(self): #This is use to define your counter and where you want to start
#         self.num = 1
#     def __iter__(self): #It will give you the object of iterator
#         return self
#     def __next__(self):

#         if self.num <= 10:
#             val = self.num
#             self.num +=1

#             return val
#         else:
#             raise StopIteration
        
# values = TopTen()

# for i in values:
#     print(i)

#--------------------------------------------------------------------

#Devorators: Is basically you can change the behaviuor of the existing function at the compile time itself

# def div(a,b):
#     print (a/b)
# #But here let suppose we want that Demoninator should always greater than numenarator
# # We can do it by modifying the div(a,b) but what if you want to don't have access of that file or you dont want to chenage it
# #In that case we use Decorators

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#             return func(a,b)
    
#     return inner
# div2 = smart_div(div)

# div2(2,4) #Traditionaly it should give 0.5 but now it with 2.0

#--------------------------------------------------------------------

#Context Manager