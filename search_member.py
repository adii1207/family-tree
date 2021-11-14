from member_node import node_array

#This function searches for name from family tree stored in list "node_array" and returns that node
def search_name(name):
    for i in range(len(node_array)):
        if name == node_array[i].data:
            return node_array[i]