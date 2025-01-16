#Generator is Basically act as a ITERATOR , means its a built in Itertor provide by python you just have to use it
# Yield is basically a keyword that converts your funtion into a Generator
def topTen():

    # yield 5
    # yield 6
    # yield 7
    # yield 8
    # yield 9
    n= 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1




values = topTen()
# print(values.__next__())
for i in values:
    print (i)