ab=int(input("Enter your account balance:"))
wa=int(input("Enter your withdrawal amount:"))
if ab>wa:
    print("Withdraw of Rs.",wa,"Sucessful!!")
    print("Remaining balance=",ab-wa)
elif ab==wa:
    print("Withdraw of Rs.",wa,"Sucessful!!")
    print("Remaining balance=",ab-wa)
else:
    print("Withdraw Unsuccessful !! Balance Low..")