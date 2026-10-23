scores = [55,80,35,90,65]

scores.append(75)
print(scores)

print("Max score",max(scores))
print("Min score",min(scores))

print("Average score",sum(scores)/len(scores))

for score in scores:
    if(score >= 80):
        print(score)
        