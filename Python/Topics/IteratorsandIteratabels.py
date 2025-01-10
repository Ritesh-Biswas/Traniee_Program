#-------------------------------------------------------Iterators and Iteratabels-------------------------------------------------------

#Iterable: Any object thats can loop over eg: list, strings
#Iterator: Any object with __iter__() and __next__() methods

nums = [7,5,6,3]

it = iter(nums)
print(it.__next__()) #--> It gives me the next value i.e 7
print(it.__next__()) #--> It will give 5

#Creating Own Interator
#Like we are creating to print 10 valuse from 1 to 10

class TopTen:
    def __init__(self): #This is use to define your counter and where you want to start
        self.num = 1
    def __iter__(self): #It will give you the object of iterator
        return self
    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num +=1

            return val
        else:
            raise StopIteration
        
values = TopTen()

for i in values:
    print(i)