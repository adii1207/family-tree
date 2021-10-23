
import sys


node_array = [] # This list stores all the exixting family members

# Creating nodes with defined properties for individual nodes of a family tree
class Node:
    def __init__(self,data):
        self.child = []
        self.data = data
        self.husband = None
        self.wife = None
        self.parent = []
        self.gender = None
    
    def __repr__(self):
        return "%s" % self.data

# This function creates node for the given name
def create_Node(name):
    return Node(name)


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
    

def GET_RELATIONSHIP(name, relation):
    # first convert the argument "relation" into lower case 
    # then look for relation defined in the program
    # if relation found return 1
    # else return 0
    relation_in_lowercase = relation.lower() # Convert the uppercase letter to lowercase letter
    if relation_in_lowercase == "son":
        if len(name.child) > 0:
            for i in name.child:
                if i.gender == "male":
                    print(i, end=" ")
            return 1
        else:
            print("PERSON NOT FOUND")
            return 0

    elif relation_in_lowercase == "daughter":
        if len(name.child) > 0:
            for i in name.child:
                if i.gender == "female":
                    print(i, end=" ")
            return 1
        else:
            print("PERSON NOT FOUND")
            return 0 

    elif relation_in_lowercase == "sister-in-law":
        if name.gender == "female":
            if len(name.parent) > 0:
                if len(name.parent[0].child) > 1:
                    for i in name.parent[0].child:
                        if i.gender == 'male' and i.wife != None:
                            print(i.wife, end=" ")
                        
            if name.husband != None:
                if len(name.husband.parent) > 0:
                    for i in name.husband.parent[0].child:
                        if i.gender == 'female':
                            print(i, end=" ")
                    return 1
            
            elif len(name.parent) > 0 and name.husband != None:
                print("PERSON_NOT_FOUND")
                return 0
                        
        elif name.gender == "male":
            if len(name.parent) > 0:
                if len(name.parent[0].child) > 1:
                    for i in name.parent[0].child:
                        if i.gender == 'male' and i.wife != None and i != name:
                            print(i.wife, end = " ")
            if name.wife != None:
                if len(name.wife.parent) != 0 and len(name.wife.parent[0].child) != 0:
                    y = name.wife.parent[0].child
                    for i in y:
                        if i == name.wife:
                            continue
                        if i.gender == "female":
                            print(i, end=" ")
                        elif i.gender == "male" and i.wife != None and i.wife != name:
                            print(i.wife, end=" ")
                    return 0

            elif len(name.parent) > 0 and name.wife != None:
                print("PERSON_NOT_FOUND")
                return 0

    elif relation_in_lowercase == "brother-in-law":
        if name.gender == "female":
            if len(name.parent) > 0:
                if len(name.parent[0].child) > 1:
                    for i in name.parent[0].child:
                        if i != name and i.gender == 'female' and i.husband != None:
                            print(i.husband, end = " ")
                        else:
                            print("PERSON_NOT_FOUND")
            if name.husband != None:
                if len(name.husband.parent) != 0 and len(name.husband.parent[0].child) != 0:
                    y = name.husband.parent[0].child
                    
                    for i in y:
                        
                        if i.gender == "male":
                            print(i, end=" ")
                        elif i.gender == "female" and i.husband != None and i.husband != name:
                            print(i.husband, end=" ")
                    return 1
            
            elif len(name.parent) > 0 and name.husband != None:
                print("PERSON_NOT_FOUND")
                return 0
                

        elif name.gender == "male":
            if len(name.parent) > 0:
                if len(name.parent[0].child) > 1:
                    for i in name.parent[0].child:
                        if i.gender == 'female' and i.husband != None:
                            print(i.husband, end = " ")
            if name.wife != None:
                if len(name.wife.parent) > 0 and len(name.wife.parent[0].child) > 1:
                    y = name.wife.parent[0].child
                    for i in y:
                        if i.gender == "male":
                            print(i, end=" ")
                        elif i.gender == "female" and i.husband != None and i.husband != name:
                            print(i.husband, end=" ")
                    return 1
        
            elif len(name.parent) > 0 and name.wife != None:
                print("PERSON_NOT_FOUND")
                return 0

    elif relation_in_lowercase == "paternal-uncle":
        if len(name.parent) > 0 and len(name.parent[0].parent) != 0:
            for i in name.parent[0].parent[0].child:
                if i.gender == "male" and i != name.parent[0]:
                    print(i, end=" ")
        else:
            print("PERSON NOT FOUND")
    
    elif relation_in_lowercase == "paternal-aunt" :
        if len(name.parent) > 0 and len(name.parent[0].parent) > 0:
            for i in name.parent[0].parent[0].child:
                if i.gender == "female" and i != name.parent[1]:
                    print(i, end=" ")
        else:
            print("PeRSON NOT FOUND")

    
    elif relation_in_lowercase == "maternal-uncle":
        if len(name.parent) > 0 and len(name.parent[1].parent) > 0:
            for i in name.parent[1].parent[0].child:
                if i.gender == "male" and i != name.parent[0]:
                    print(i, end=" ")
        else:
            print("PERSON NOT FOUND")


    elif relation_in_lowercase == "maternal-aunt":
        if len(name.parent) > 0 and len(name.parent[1].parent) > 0:
            for i in name.parent[1].parent[0].child:
                if i.gender == "female" and i != name.parent[1]:
                    print(i, end=" ")
        else:
            print("PERSON NOT FOUND")


    elif relation_in_lowercase == "siblings":
        if len(name.parent) > 0 and len(name.parent[0].child) > 1:
            for i in name.parent[0].child:
                if i != name:
                    print(i)
        else:
            print(None)
    else:
        print("PERSON NOT Found")
    

if __name__ == "__main__":

    input_file = sys.argv[1]

    #This function initialises the family tree
    def initialize_family():
        king_shan = create_Node('king_shan')
        king_shan.gender = "male"
        queen_anga = create_Node("queen_anga")
        queen_anga.gender = "female"
        king_shan.wife = queen_anga
        queen_anga.husband = king_shan
        Chit = create_Node("Chit")
        ADD_CHILD(queen_anga, Chit, "male")
        Ish = create_Node("Ish")
        ADD_CHILD(queen_anga, Ish, "male")
        Vich = create_Node("Vich")
        ADD_CHILD(queen_anga, Vich, "male")
        Aras = create_Node("Aras")
        ADD_CHILD(queen_anga, Aras, "male")
        Satya = create_Node("Satya")
        ADD_CHILD(queen_anga, Satya, "female")
        Amba = create_Node("Amba")
        Amba.gender = "female"
        Lika = create_Node("Lika")
        Lika.gender = "female"
        Chitra = create_Node("Chitra")
        Chitra.gender = "female"
        Vyan = create_Node("Vyan")
        Vyan.gender = "male"
        Chit.wife = Amba
        Amba.husband = Chit
        Vich.wife = Lika
        Lika.husband = Vich
        Aras.wife = Chitra
        Chitra.husband = Aras
        Satya.husband = Vyan
        Vyan.wife = Satya
        Dritha = create_Node("Dritha")
        Tritha = create_Node("Tritha")
        Vritha = create_Node("Vritha")
        ADD_CHILD(Amba, Dritha, "female")
        ADD_CHILD(Amba, Tritha, "female")
        ADD_CHILD(Amba, Vritha, "male")
        Jaya = create_Node("Jaya")
        Jaya.gender = "male"
        Dritha.husband = Jaya
        Jaya.wife = Dritha
        Yodhan = create_Node("Yodhan")
        ADD_CHILD(Dritha, Yodhan, "male")
        Vila = create_Node("Vila")
        Chika = create_Node("Chika")
        ADD_CHILD(Lika, Vila, "female")
        ADD_CHILD(Lika, Chika,"female")
        Jnki = create_Node("Jnki")
        Ahit = create_Node("Ahit")
        ADD_CHILD(Chitra, Jnki, "female")
        ADD_CHILD(Chitra, Ahit, "male")
        Arit = create_Node("Arit")
        Arit.gender = "male"
        Jnki.husband = Arit
        Arit.wife = Jnki
        Laki = create_Node("Laki")
        Lavnya = create_Node("Lavnya")
        ADD_CHILD(Jnki, Laki, "male")
        ADD_CHILD(Jnki, Lavnya, "female")
        Asva = create_Node("Asva")
        Vyas = create_Node("Vyas")
        Atya = create_Node("Atya")
        ADD_CHILD(Satya, Asva, "male")
        ADD_CHILD(Satya, Vyas,"male")
        ADD_CHILD(Satya, Atya, "female")
        Satvy = create_Node("Satvy")
        Satvy.gender = "female"
        Asva.wife = Satvy
        Satvy.husband = Asva
        Vasa = create_Node("Vasa")
        ADD_CHILD(Satvy, Vasa, "male")
        Krpi = create_Node("Krpi")
        Krpi.gender = "female"
        Vyas.wife = Krpi
        Krpi.husband = Vyas
        Kriya = create_Node("Kriya")
        Krithi = create_Node("Krithi")
        ADD_CHILD(Krpi, Kriya, "male")
        ADD_CHILD(Krpi, Krithi, "female") 
    
        
        node_array.append(king_shan)
        node_array.append(queen_anga)
        node_array.append(Chit)
        node_array.append(Ish)
        node_array.append(Vich)
        node_array.append(Aras)
        node_array.append(Satya)
        node_array.append(Amba)
        node_array.append(Lika)
        node_array.append(Chitra)
        node_array.append(Vyan)
        node_array.append(Dritha)
        node_array.append(Jaya)
        node_array.append(Tritha)
        node_array.append(Vritha)
        node_array.append(Vila)
        node_array.append(Chika)
        node_array.append(Arit)
        node_array.append(Jnki)
        node_array.append(Ahit)
        node_array.append(Satvy)
        node_array.append(Asva)
        node_array.append(Krpi)
        node_array.append(Vyas)
        node_array.append(Atya)
        node_array.append(Yodhan)
        node_array.append(Laki)
        node_array.append(Lavnya)
        node_array.append(Vasa)
        node_array.append(Kriya)
        node_array.append(Krithi)    
    
    initialize_family()
    
    #This function searches for name from family tree and returns that node
    def search_name(name):
        for i in range(len(node_array)):
            if name == node_array[i].data:
                return node_array[i]

    # function_call recieves input from test_file.txt
    def function_call(*args):
        Search_result = search_name(args[0][1])
        if args[0][0] == "ADD_CHILD" and Search_result in node_array:
            x = create_Node(args[0][2])
            a = ADD_CHILD(Search_result, x, args[0][3].lower())
            if a == 0:
                print("CHILD_ADDITION_FAILED")
                return 0
            else:
                print("CHILD_ADDITION_SUCCEEDED")
                node_array.append(a)   
                return 0

        elif args[0][0] == "GET_RELATIONSHIP" and Search_result in node_array:
            GET_RELATIONSHIP(Search_result, args[0][2])
            print()

        else:
            print("PERSON_NOT_FOUND")
    
    # Reading the test_file.txt 
    with open(input_file, 'r') as file:
        lines = file.readlines()
        if lines == []:
            print("add something to test.txt file")

        else:
            for line in lines:
                function_call(line.split())

    
        