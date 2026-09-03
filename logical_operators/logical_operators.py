marks=int(input("Enter your marks:"))
attendance=int(input("Enter your attendance:"))
#AND
if marks>=40 and attendance>=75:
    print("Eligible for exam")
#OR
if marks>=90 or marks ==100:
    print("Excellent performance")
#NOT
if not marks>=40:
    print("You have failed")