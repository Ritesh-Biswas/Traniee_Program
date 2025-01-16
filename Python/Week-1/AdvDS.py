#---------------List & Tuples------------------

#-> Lists 
# List is sort of equivalent to Arrays

marks = [123.2, 145.2, 134,150,144]
# In list we can store the different type of elments togather like [float,string,integer]
#Lists are IMMUTABLE

#-> List Slicing
#list_name[ staring_index : ending_index ]
# print(marks[1:3])
#-> List Methods ->list.append(4) add one elemtne to the end
#                ->list.sort() sort in ascending order
#                ->list.sort(reverse=True) sort in descending order
#                ->list.reverse() reverse the lise
#                ->list.insert(idx,el)
#                ->list.remove(1) it removes the first occurnce of the element
#                ->list.pop(idx) it remove the element ate the index


#-> Tuples
#Tuples are IMMUTABLE 

marks2 = (2,1,3,4,5)
#->Tuple Methods -> marks2.index(el)
#                -> marks2.count(el)