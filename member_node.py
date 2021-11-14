node_array = [] # This list stores all the existing family members

# Creating nodes with defined properties for individual nodes of a family tree
# a node has properties of having:
#               child
#               husband
#               wife
#               parent
#               gender
# data reflects the name of node itself
class Node:
    def __init__(self,data):
        self.child = []
        self.data = data
        self.husband = None
        self.wife = None
        self.parent = []
        self.gender = None
    
    # this function returns the name of the node if the node exist
    def __repr__(self):
        return "%s" % self.data

# This function creates node for the given name
def create_Node(name):
    return Node(name)
