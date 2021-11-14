def daughter(name):
    #looks for child property of "name" with gender female 
    if len(name.child) > 0:
        for i in name.child:
            if i.gender == "female":
                print(i, end=" ")
        return 1
    else:
        print("PERSON NOT FOUND")
        return 0 
