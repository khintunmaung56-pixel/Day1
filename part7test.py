def calculate_total(scores):
    return sum(scores)
def calculate_average(scores):
    return sum(scores)/len(scores)

def count_passed(scores):
    passingScore = 0
    fallingScore = 0
    for score in scores:
         if score>=40:
             passingScore+=1
    return passingScore

def classify_grade(marks):
    if marks<0 or marks >100:
        print("invald marks")
    elif marks>=80:
        print("Excellent")
    elif marks>=60:
        print("good")
    elif marks>=40:
        print("passed")
    else:
        print("fail")

scores=[50,60,40,30]
print(calculate_average(scores))
print(calculate_total(scores))
print(count_passed(scores))

for marks in scores:
    classify_grade(marks)