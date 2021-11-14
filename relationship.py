from relation_paternal_aunt import paternal_aunt
from relation_patrenal_uncle import patrenal_uncle
from relation_maternal_uncle import maternal_uncle
from relation_maternal_aunt import maternal_aunt
from relation_son import son
from relation_daughter import daughter
from relation_siblings import siblings
from relation_sister_in_law import sister_in_law
from relation_brother_in_law import brother_in_law



def GET_RELATIONSHIP(name, relation):
    # first convert the argument "relation" into lower case 
    # then look for relation defined in the program
    # if relation found return 1
    # else return 0
    relation_in_lowercase = relation.lower() # Convert the uppercase letter to lowercase letter
    
    # condition for finding son
    if relation_in_lowercase == "son":
        son(name)
    
    # condition for finding daughter
    elif relation_in_lowercase == "daughter":
        daughter(name)


    # condition for finding sister-in-law
    elif relation_in_lowercase == "sister-in-law":
        sister_in_law(name)
        

    elif relation_in_lowercase == "brother-in-law":
        brother_in_law(name)

    elif relation_in_lowercase == "paternal-uncle":
        patrenal_uncle(name)
        
    
    elif relation_in_lowercase == "paternal-aunt" :
        paternal_aunt(name)

    
    elif relation_in_lowercase == "maternal-uncle":
        maternal_uncle(name)


    elif relation_in_lowercase == "maternal-aunt":
        maternal_aunt(name)

    elif relation_in_lowercase == "siblings":
        siblings(name)
        
    else:
        print("PERSON NOT Found")