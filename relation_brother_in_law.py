def brother_in_law(name):
    if name.gender == "female":
        # looks for brother-in-law in same family
        #    check for parents of "name":
        #        check for siblings of "name":
        #            give name of husband of female siblings
        if len(name.parent) > 0:
            if len(name.parent[0].child) > 1:
                for i in name.parent[0].child:
                    if i != name and i.gender == 'female' and i.husband != None:
                        print(i.husband, end = " ")
                    else:
                        print("PERSON_NOT_FOUND")
        # looks for brother-in-law in husbands family 
        # check for husband parent
        # #    check for husband's siblings with gender as male and print them 
        #    check for husband's siblings with gender as female and find their husband
        if name.husband != None:
            if len(name.husband.parent) != 0 and len(name.husband.parent[0].child) != 0:
                
                for i in name.husband.parent[0].child:
                    
                    if i.gender == "male":
                        print(i, end=" ")
                    elif i.gender == "female" and i.husband != None and i.husband != name:
                        print(i.husband, end=" ")
                return 1
                
        # condition for no brother-in-law
        # no parents and not spouse
        elif len(name.parent) > 0 and name.husband != None:
            print("PERSON_NOT_FOUND")
            return 0
                

    elif name.gender == "male":
        # looks for brother-in-law in same family
        #    check for parents of "name":
        #        check for siblings of "name":
        #            give name of husband of female siblings
        if len(name.parent) > 0:
            if len(name.parent[0].child) > 1:
                for i in name.parent[0].child:
                    if i.gender == 'female' and i.husband != None:
                        print(i.husband, end = " ")
        # looks for brothter-in-law in husbands family 
        # check for wife parent
        #    check for wives siblings with gender as male and print them    
        #    check for wives siblings with gender as female and find their husbands                 
        if name.wife != None:
            if len(name.wife.parent) > 0 and len(name.wife.parent[0].child) > 1:
                y = name.wife.parent[0].child
                for i in y:
                    if i.gender == "male":
                        print(i, end=" ")
                    elif i.gender == "female" and i.husband != None and i.husband != name:
                        print(i.husband, end=" ")
                return 1
        # condition for no brother-in-law
        # no parents and not spouse
        elif len(name.parent) > 0 and name.wife != None:
            print("PERSON_NOT_FOUND")
            return 0