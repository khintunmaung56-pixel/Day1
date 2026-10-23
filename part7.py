def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)

scores = [45,75,85]
result=calculate_average(scores)
print(result)