#-------------------------------------------------------Context Manager-------------------------------------------------------

#Context Manager : It is a constructor that basically allow you to manage resource efficiently.
#It handles SETUP, CLEANUP actions automatically.

# There is two type -> 1. Built-in, 2. Custom

#Its practically use in Database Connection and FIle Handling

#----------------Built-In--------------------

#
# with sqllit3.connect("example.db") as connection:
#     make_conne = connection.db
#
#
# with open("hello.txt","w") as file:
#     file.write("Fuck you marco")

#----------------Custom Context Manager--------------------
#__enter__() -> Runs at the start ('with' block)
#__exit__() -> Runs at the end for cleanup