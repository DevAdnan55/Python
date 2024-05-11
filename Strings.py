# Three ways to make a string
str1 = "This is a string";
str2 = """This is a string""";
str3 = 'This is a string';

# Why there are three types of string ?
Str4 = "This is a string, so you dont't need to check its type";
str5 = 'This is a string, so you dont"t need to check its type';

# To format a string we use escape sequence of characters.
str6 = "This is a string.\nwe are creating it in python."; # \n = New line
# print(str6);

# Concatenation: Combining two strings together.
len1 = "Real ";
len2 = "Madrid";
final_Str = len1 + len2 + " will win the UCL"; # Spaces will also be counted in lenght.
print(final_Str);
print(len(final_Str)); # This function will calculate the length of the string.

# Sting Functions.

# 1] Indexing 
ind = "Max Verstappen"
print(ind[4]);
ind[3] = "_";
print(ind); # This will genearte error bcoz we can only access a characte and cannot assign anything to it.

# 2] Slicing 
slc = "MercedesAMG"
print(slc[8:11]); # Note 8 is included but 11 is excluded.
print(slc[8:len(slc)]); 
print(slc[8:]); # [8:11]
print(slc[:8]); # [0:8]

slc2 = "Apple";
print(slc2[-5:-2]); # Negative Indexing
print(slc2[:-2]);

# endsWith("ege.") = Returns true if the string ends with the given value.
end_Value = "I am studing python from ApnaCollege." 
print(end_Value.endswith("ege.")); # True
print(end_Value.endswith("Apn")); # False

# capitalize() = It will capitalize the 1st char of the string.
cap = "i am studing python from ApnaCollege." 
print(cap.capitalize()); # This will only change the original text one time.
cap = cap.capitalize(); #This will permanently change it.
print(cap);

# replace("old", "new") =  Will repace old value with new ones.
change = "I am studing python from ApnaCollege." 
print(change.replace("o", "a")); # Temporary.
change = change.replace("python", "JavaScript"); # Permanent.
print(change);

# find("word") = Returns 1st index of 1st occurrer.
search = "I am studing python from ApnaCollege."
print(search.find("o")); # Ans = 17
print(search.find("python")); # Ans = 13

# count("am") = Counts the occourrence of the given value.
occ = "AM at 4 AM, they realized they had forgotten to set their alarm clock for the crucial 4 AM";
print(occ.count("AM")); # Ans = 3.
