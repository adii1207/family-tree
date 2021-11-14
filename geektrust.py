import sys
from child_add import ADD_CHILD
from relationship import GET_RELATIONSHIP
from member_node import *
from Initial_family import family
from search_member import search_name
    
if __name__ == "__main__":

    input_file = sys.argv[1] # recieving file as an input argument with input commands    

    # family() function initialises the initail family members of the family
    family()

    # function_call recieves input from test_file.txt
    def function_call(*args):
        Search_result = search_name(args[0][1])
        if args[0][0] == "ADD_CHILD" and Search_result in node_array:
            x = create_Node(args[0][2])
            adding_child = ADD_CHILD(Search_result, x, args[0][3].lower())
            if adding_child == 0:
                print("CHILD_ADDITION_FAILED")
                return 0
            else:
                print("CHILD_ADDITION_SUCCEEDED")
                node_array.append(adding_child)   
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

    
        