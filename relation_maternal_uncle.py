def maternal_uncle(name):
    # looks for sibling of mother with gender male
    if len(name.parent) > 0 and len(name.parent[1].parent) > 0:
        for i in name.parent[1].parent[0].child:
            if i.gender == "male" and i != name.parent[0]:
                print(i, end=" ")
    else:
        print("PERSON NOT FOUND")