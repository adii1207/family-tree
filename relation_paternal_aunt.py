def paternal_aunt(name):
    #looks for sibling of father with gender female
    if len(name.parent) > 0 and len(name.parent[0].parent) > 0:
        for i in name.parent[0].parent[0].child:
            if i.gender == "female" and i != name.parent[1]:
                print(i, end=" ")
    else:
        print("PERSON NOT FOUND")