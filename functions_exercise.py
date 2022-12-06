'''
Task: write a function which takes 3 assessment scores, out of 100, and returns the average percentage. 
Use this function to calculate a percentage, and print this percentage and a grade based on the percentage
'''

def grade_calc(*scores):
    avg = sum(scores) // len(scores)
    bound = avg - (avg % 10)
    if bound >= 80:
        grade = 'A'
    elif bound == 70:
        grade = 'B'
    elif bound == 60:
        grade = 'C'
    else:
        grade = 'F'
    return avg, grade

scores = []

while len(scores) < 3:
    scores.append(int(input("Enter a score: ")))

avg, grade = grade_calc(*scores)
print("You scored", f"{avg}%", "and achieved a grade", grade)
