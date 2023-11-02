def my_function():
    x=10 #x is a local variable
    print(x)

my_function()# accessing x outside the function


x=10 #x is global variable
def my_function():
    print(x) #accessing the global variable


my_function()
#local scope:
#variables defined within a function are local to that function and can only be accesezd within that function

#non-local scope:
#if you want to modify a global variable from within a function you can use the global keyword to indicate that you are working with the global variable


x=10 #global variable
def modify_global():
    global x # non-local scope variable . by using global keyword
    x=20

modify_global()
print(x)