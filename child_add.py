def ADD_CHILD(Mother_name, Child_name, Gender):
    #check if mother is female and has a husband or not
    #if above condition is true
    #set the gender of child accordingly as the "Gender" parameter of this function
    #add child name to child property of the mother and father
    #add mother and father name to child's parent property 

    if Mother_name.gender == "female" and Mother_name.husband != None:
        if Gender == "male":
            Child_name.gender = "male"
            Mother_name.child.append(Child_name)
            Mother_name.husband.child = Mother_name.child
            Child_name.parent.append(Mother_name.husband)
            Child_name.parent.append(Mother_name) 
            return Child_name

        elif Gender == "female":
            Child_name.gender = "female"
            Mother_name.child.append(Child_name)
            Mother_name.husband.child = Mother_name.child
            Child_name.parent.append(Mother_name.husband)
            Child_name.parent.append(Mother_name)
            return Child_name
            
        else:
            return 0
    else:
        return 0
