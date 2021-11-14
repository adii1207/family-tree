
from child_add import ADD_CHILD
from member_node import *
from search_member import search_name
from SET_GENDER import set_gender
from SET_spouse import spouse


def family():
    def initial_family(*args):

        if args[0][0] == "create_Node":
            args[0][1] = create_Node(args[0][1])
            node_array.append(args[0][1])
        
        elif args[0][0] == "ADD_CHILD" and search_name(args[0][1]) in node_array:
            ADD_CHILD(search_name(args[0][1]), search_name(args[0][2]), args[0][3])

        elif args[0][0] == "SET_GENDER" and search_name(args[0][1]) in node_array:
            set_gender(args[0][1], args[0][2])

        elif args[0][0] == "wife" and search_name(args[0][1]) in node_array:
            if search_name(args[0][2]) in node_array:
                spouse(args[0][0], search_name(args[0][1]), search_name(args[0][2]))

        elif args[0][0] == "husband" and search_name(args[0][1]) in node_array:
            if search_name(args[0][2]) in node_array:
                spouse(args[0][0], search_name(args[0][1]), search_name(args[0][2]))
                
    with open("initial_members.txt", 'r') as file:
        lines = file.readlines()
        if lines == []:
            print("add something to test.txt file")

        else:
            for line in lines:
                initial_family(line.split())