print("----Voting Checker----")
age= int(input("Enter your age:"))

if age>=18:
    print("you can  vote")
    print("you are  eligible ")
elif age <= 18 and age >=3:
    print("you can not vote")
    print("you are not eligible")
else:
    print("you are child")


print("Thank you")