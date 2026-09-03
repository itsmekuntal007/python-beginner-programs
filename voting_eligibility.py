age=int(input("Enter the age of the person:"))
c=input("Enter the nationality of the person:")
if c.lower()=='indian':
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote due to age")
elif c.lower()!='indian' and age<18:
    print("Not eligible due to both criteria not met")
else:
    print("Not eligible to vote due to different nationality")