# # if-elif-else (Syntax)
# age = 12;

# if(age >= 18):
#     print("Eligible to vote and drive") # if statement will aways check the conditional.
# elif(age <= 18):
#     print("Sorry you are not Eligible") # elif statement will only check the condition, when if statement is false

# light = "green";

# if(light == "red"): 
#     print("Stop") # You can use if statement in the start and multiple times in a program
# elif(light == "green"):
#     print("Go")  # You can use elif statement multiple times in a program
# elif(light == "yellow"):
#     print("Look") # You can use else statement only one time and in the end of your program 
# else:
#     print("The light is  broken") # Note: The tab given after each statement is called Indetation. 

marks = int(input("Enter your marks : "))

if(marks > 100):
    grade = "Invvalid marks"
elif(marks >= 90):
    grade = "A"
elif(marks < 90 and marks >= 80):
    grade = "B"
elif(marks < 80 and marks >= 70):
    grade = "C"
elif(marks < 70 and marks >= 60):
    grade = "D"
elif(marks < 60 and marks >= 50):
    grade = "E"
else:
    grade = "Unfortunately you have failed"

print("Grade of the student => ",grade);

