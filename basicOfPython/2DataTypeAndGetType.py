x, y, z = 1, 1.1, "abc"
print(x)
print(y)
print(z)

# TypeError: can only concatenate str (not "int") to str
# print ("Hi : "+ x)

# This will have no issue as we are trying to concat string with string values
print("Hi : " + z)

# we can use .formate for this and this will have no issue
print ("Hi : {}, {}, {}".format(x, y, z))

# we can use f-string for this and this will have no issue
print (f"Hi : {x}, {y}, {z}")

# to know the datatype of any variable
print(type(x))
print(type(y))
print(type(z))