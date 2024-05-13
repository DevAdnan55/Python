# Tuples are immutable
tup = (2, 1, 3, 1)
print(type(tup))

tup_1 = (1) # This will be considered as int if you dont put comma after the element
print(type(tup_1)) 
tup_2 = ("Hello")
print(type(tup_2))

tup_1 = (1, ) # This will be considered as tuple
print(type(tup_1))
tup_2 = ("Hello", )
print(type(tup_2))

# Tuple Methods

# Index Method
tup_3 = (1, 2, 3, 4, 2, 5, 2)
print(tup_3.index(2)) # The first occurance of 2 is at 1 index 

# Count Method
print(tup_3.count(2)) # It will count the amount of time 2 is there in a tuple 