#-------------------------------------------------------Decorators-------------------------------------------------------

#Decorators: Is basically you can change the behaviuor of the existing function at the compile time itself

def div(a,b):
    print (a/b)
#But here let suppose we want that Demoninator should always greater than numenarator
# We can do it by modifying the div(a,b) but what if you want to don't have access of that file or you dont want to chenage it
#In that case we use Decorators

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
            return func(a,b)
    
    return inner
div2 = smart_div(div)

div2(2,4) #Traditionaly it should give 0.5 but now it with 2.0