#1 adding integer and float
num_int = 123
num_flo = 1.23
#We add two variables num_int and num_flo, storing the value in num_new
num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
# In the output, we can see the data type of num_int is an integer
# while the data type of num_flo is a float
print("Value of num_new:",num_new) #124.23
print("datatype of num_new:",type(num_new))

#2 adding a string and an integer
num_int = 123
num_str = "456"
print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))
#print(num_int+num_str) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
