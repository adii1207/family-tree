def son(name):
    #looks for child property with gender male 
    if len(name.child) > 0:
            for i in name.child:
                if i.gender == "male":
                    print(i, end=" ")
            return 1
    else:
        print("PERSON NOT FOUND")
        return 0