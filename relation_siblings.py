def siblings(name):
    # looks for siblngs and prints their name
    if len(name.parent) > 0 and len(name.parent[0].child) > 1:
        for i in name.parent[0].child:
            if i != name:
                print(i)
    else:
        print("NONE")