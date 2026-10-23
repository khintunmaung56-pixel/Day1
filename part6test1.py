scores=[70,85,60,90,45,30]
total=0
for score in scores:
    total +=score

average =total/len(scores)

print("Total:",total)
print("Average:",average)
passingScore=0
fallingScore=0
for score in scores:
    if score>=40:
        passingScore+=1
    if score<=39:
        fallingScore+=1

print("Numebr of pass:",passingScore)
print("Number of fall:",fallingScore)