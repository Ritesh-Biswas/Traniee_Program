#-------------------------------------------------------Generator Expressions-------------------------------------------------------
squares_gen = (x**2 for x in range(10))
print("This is for Generator Expressions")
for num in squares_gen:
    print(num)