# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movie_1 = input("Enter your  first movie => ")
movie_2 = input("Enter your  second movie => ")
movie_3 = input("Enter your  third movie => ")
print("\nYour top 3 favorite movies are :-")
fav_movies = [movie_1, movie_2, movie_3]
print(fav_movies)


movies = []
movies.append(input("Enter your  first movie => "))
movies.append(input("Enter your  second movie => "))
movies.append(input("Enter your  third movie => "))

print("\nYour top 3 favorite movies are :-")
print(movies)

# WAP to check if a list contains a palindrome of elements.

list1 = [1, 2, 3, 2, 1]
list2 = ['a', 'b', 'c', 'b', 'a']

copy_list2 = list2.copy()
copy_list2.reverse()

if(list2 == copy_list2):
    print("Palindrome")
else:
    print("Not Palindrome")

# WAP to count the number of student with "A" grade in the following tuple
#       ("C", "D", "A", "A", "B", "B", "A")

grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

# WAP to store the above value in a list & sort them from "A" to "D"

list_sort = ["C", "D", "A", "A", "B", "B", "A"]
list_sort.sort()
print(list_sort)

