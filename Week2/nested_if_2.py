place=input("Where should I look?")

if place=="in the bedroom":
    print("Where in the bedroom should I look?")
    location=input()
    if location=="under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

elif place=="in the bathroom":
    print("Where in the bathroom should I look?")
    location=input()
    if location=="in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

elif place=="in the living room":
    print("Where in the living room should I look?")
    location=input()

    if location=="on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")

else:
    print("I do not know where that is but I will keep looking.")