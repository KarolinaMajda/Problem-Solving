print("What should I do (recover/study)? ")
activity=input()
if activity=="recover":
    act1=input("How would you like to recover(sleep/socialise? ")

    if act1== "sleep":
        print("zzzZZzz")
    else:
        print("I will text my friends!")
else:
    print("I will study")
    study=input("What subject do you want to study? (networking/Cyber) ")
    if study=="networking":
        print("study intro to networks")
    else:
        print("study cyber")
    print("activity completed!")


