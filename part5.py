marks=float(input("Enter your mark"))
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

