'''
Task: Write a program which takes a user's name and year of birth,
and prints out a message greeting the user and stating their age
(calculated simply as current year - birth year for now)
'''

name = input("Please enter your name: ")
birth_year = int(input("Please enter your year of birth: "))

print("Hello,", name, "you are", 2022 - birth_year, "years old")