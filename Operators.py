# Arithmetic Operators
a = 5;
b = 2;

print(a + b);
print(a - b);
print(a / b);
print(a * b);
print(a % b);  # % = Modulo, will generate the remainder
print(a ** b); # a^b 

#Relational/Comparison Operator 
#Will always give the output in True or False
a = 50;
b = 20; 

print(a == b); # Equal to, Ans False
print(a != b); # Not equal to, Ans True
print(a >= b); # a is greater than or equal to b, Ans True
print(a > b);  # True
print(a <= b); # a is less than or equal to b, Ans False
print(a < b);  # False

#Assignment Operator
num = 5;
num += 10; # Will add 10 with the current num value, Ans 15
print("num :", num);

num -= 10; # Will substract 10 with the current num value, Ans 5
print("num :", num);

num *= 10; # Will mutiply 10 with the current num value, Ans 50
print("num :", num);

num /= 10; # Will divide 10 with the current num value, Ans 5
print("num :", num);

num %= 10; # Will divide 10 with the current num value and generate remainder, Ans 5
print("num :", num);

num **= 10; # Will calculate with current value of num^10, Ans 9765625 
print("num :", num);

#Logical Operators
a = 50;
b = 20;
print(not False); #not operator works on a operand
print(not (a >= b)); # Not operator: inverts the value 

val1 = True;
val2 = False;
print("and operator:", val1 and val2); # Works on 2 operands
# and Operator : If both the value is True, then the ans is True 
#              : If any one value is False, then the ans is False

print("or operator:", (a == b) or (a > b)); # Works on 2 operands
# and Operator : If both the value is False, then the ans is False 
#              : If any one value is True, then the ans is True