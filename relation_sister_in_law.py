def sister_in_law(name):
    if name.gender == "female":
            # looks for sister-in-law in same family
            #    check for parents of "name":
            #        check for siblings of "name":
            #            give name of wives of male siblings
            if len(name.parent) > 0:
                if len(name.parent[0].child) > 1:
                    for i in name.parent[0].child:
                        if i.gender == 'male' and i.wife != None:
                            print(i.wife, end=" ")

            # looks for sister-in-law in husbands family 
            #check for husband parent 
            #    check for husband's siblings with gender as male and find their wives            
            if name.husband != None:
                if len(name.husband.parent) > 0:
                    for i in name.husband.parent[0].child:
                        if i.gender == 'female':
                            print(i, end=" ")
                    return 1
            
            # condition for no sister-in-law
            # no parents and not spouse
            elif len(name.parent) > 0 and name.husband != None:
                print("PERSON_NOT_FOUND")
                return 0
                        
               
    elif name.gender == "male":
        # looks for sister-in-law in same family
        #    check for parents of "name":
        #        check for siblings of "name":
        #            give name of wives of male siblings
        if len(name.parent) > 0:
            if len(name.parent[0].child) > 1:
                for i in name.parent[0].child:
                    if i.gender == 'male' and i.wife != None and i != name:
                        print(i.wife, end = " ")

        # looks for sister-in-law in husbands family 
        #check for wife parent
        #    check for wives siblings with gender as female and print them
        #    check for wives siblings with gender as male and find their wives
        if name.wife != None:
            if len(name.wife.parent) != 0 and len(name.wife.parent[0].child) != 0:
                #y = name.wife.parent[0].child
                for i in name.wife.parent[0].child:
                    if i == name.wife:
                        continue
                    if i.gender == "female":
                        print(i, end=" ")
                    elif i.gender == "male" and i.wife != None and i.wife != name:
                        print(i.wife, end=" ")
                return 0

        # condition for no sister-in-law
        # no parents and not spouse
        elif len(name.parent) > 0 and name.wife != None:
            print("PERSON_NOT_FOUND")
            return 0