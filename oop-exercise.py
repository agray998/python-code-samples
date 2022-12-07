class Student():
    def __init__(self, class_, age, name = "student"):
        self.name = name
        self.class_ = class_
        self.age = age
    
    @staticmethod
    def grade_calc(*scores):
        avg = sum(scores) // len(scores)
        gradebounds = {100:"A*", 90:"A*", 80:"A", 70:"B", 60:"C"}
        bound = avg - (avg % 10)
        grade = gradebounds.get(bound, "F")
        return avg, grade

name = input("Please enter a name: ")
class_ = input(f"What subject does {name} study? ")
age = int(input(f"Please enter {name}'s age: "))

student1 = Student(name = name, class_ = class_, age = age)

scores = []

while len(scores) < 3:
    scores.append(int(input("Enter an assessment score: ")))

avg, grade = student1.grade_calc(*scores)
print(student1.name, f"scored {avg}% and achieved a grade", grade)