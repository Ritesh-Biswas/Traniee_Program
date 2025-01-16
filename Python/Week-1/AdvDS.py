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

#---------------Dictionary & Sets------------------
#-> Dicitonary
#Dictionary is used to store the data values in key:value pair
#Tehy are unorderd, mutable and dont's allow duplicasy

dict = {
    "name" : "Ritesh",
    "CGPA" : 9.6,
    "marks" : [85,77,80]
}

#There is a Nested Dictonary 
#-> Dictonary Methods ->dict.keys() it return all the keys
#                     ->dict.values() it return all values
#                     ->dict.items() it return all the (key,val) pairs as tuples
#                     ->dict.get("key") return the key according th value
#                     ->dict.update(newDict) insert specific item to the dictionary 

#-> Sets
#Set is the collection of the unsorted items
#Each item should be unique and immutable

nums = {1,2,3,4}
#-> Sets Methods ->nums.add(el) add an element
#                ->nums.remove(el) removes the element
#                ->nums.clear() empty the set by clearing the sxisting elemsnts
#                ->nums.pop() removes the random value
#                ->nums.union(set2) combines bothe the sets values and return new set
#                ->nums.intersection(set2) combines the common values fro both sets and return new set
