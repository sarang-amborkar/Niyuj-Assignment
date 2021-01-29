num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))
num_sum = num_int + num_str
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

# int variable
a = 5

# typecast to float
n = float(a)
print(n)
print(type(n))

# int variable
a = 5.9

# typecast to int
n = int(a)
print(n)
print(type(n))

# int variable
a = 5
# typecast to str
n = str(a)
print(n)
print(type(n))

# string variable
a = "5"
# typecast to int
n = int(a)
print(n)
print(type(n))

# string variable
a = "5.9"
# typecast to float
n = float(a)
print(n)
print(type(n))