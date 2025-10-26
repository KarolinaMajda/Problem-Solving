
cover_type=input("What type of cover does the book have? ")
if cover_type=="soft":
    bound=input("Is the book perfect bound? ")
    if bound=="yes":
        print("Soft cover, perfect bound are very popular! ")
    else:
        print("soft cover, with coils or stitches are great for short books")
else:
    print("Books with hard cover can be more expensive")