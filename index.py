print("Welcome back Patrick")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("The sum of the two numbers is: ", int(num1) + int(num2))

#list Data Types
languages = ["Python", "Java", "C++", "JavaScript", "PHP"]

print("The first language is: ", languages[0]) # The first language is:  Python
print("The second language is: ", languages[1]) # The second language is:  Java
print("The third language is: ", languages[2])  # The third language is:  C++
print("The fourth language is: ", languages[3])  # The fourth language is:  JavaScript
print("The fifth language is: ", languages[4])

#multiple data types to multiple variables
name, age, country = str(input("enter name")), int(input("enter age")), str(input("enter country"))
print("My name is: ", name) # My name is:  Patrick
print("I am ", age, " years old") # I am  22  years old 
print("I am from: ", country) # I am from:  South Afric