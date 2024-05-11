# Wap to check if a number entered by the user is odd or even. 
num = int(input("Enter your number : "));
rem = num % 2;

if(num == 0):
    print("Number is EVEN ")
else:
    print("Number is ODD ")

# WAP to find the greatest of 3 numbers entered by user.
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if(a >= b and a >= c):
    print("First number is the greatest")
elif(b >= c):
    print("Second number is the greatest")
else:
    print("Third number is the greatest")

# WAP to check if a number is a multiple of 7 or not
giv = int(input("Enter your number : "))

if(giv % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a multiple")