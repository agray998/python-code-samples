'''
Task: Write a program which takes in a mark out of 100, and prints:
"A*" if the mark is greater than 85
"A" if the mark is between 75 and 85
"lower than an A" if the mark is less than 75
Stretch goal: reject invalid inputs (outside of the range 0 - 100, 
or non-numeric strings)
'''

invalid = True
tries = 0

while invalid and tries < 3:
    mark = input("Please enter a mark out of 100: ")
# Stretch goal stuff
    if not mark.isnumeric() or not int(mark) <= 100:
        print("Invalid input!")
        tries += 1
    else:
        # basic solution
        mark = int(mark)

        if mark > 85:
            print("A*")
        elif mark >= 75:
            print("A")
        else:
            print("lower than an A")
        invalid = False