# Note :- Strings are immutable & Lists are mutable.

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])

student = ["karna", 95.4, 17, "Delhi"]
print(student[0])
student[0] = "Arjun"
print(student)
print(student[1:4])
print(student[0:4])
print(student[0:len(student)])

# List Methods

# Append Method
list = [2, 1, 3] 
list.append(4) # Adds one element at the end.
print(list)

# Sort Method
list = [2, 1, 3] 
str_List = ["banana", "litchi", "apple"] 
char_list = ['z', 'v', 'g', 'a', 'f', 'b', 'c']

list.sort() # It will sort the elements in ascending order. 
str_List.sort() # It will sort based on the char.
char_list.sort()
print(list)
print(str_List)
print(char_list)

list.sort(reverse=True) # It will sort the elements in descending order. 
str_List.sort(reverse=True)
char_list.sort(reverse=True)
print(list)
print(str_List)
print(char_list)

# Reserve Method
list.reverse() # Reverses list
char_list.reverse()
print(list)
print(char_list)

# Insert Method
list = [2, 1, 3] 
char_list = ['z', 'v', 'g', 'a', 'f', 'b', 'c']
list.insert(1, 5)
char_list.insert(3, 'y')
print(list)
print(char_list)

# Remove Method
list = [2, 1, 3, 1, 1, 4]
list.remove(1) # Removes first occurance of element
print(list)

# Pop Method
list.pop(3) # Removes element at idx
print(list)