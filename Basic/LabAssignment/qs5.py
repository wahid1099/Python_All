
def create_list():
    x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
    # d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}


    new_list=[]
    for key, val in x.items(): 
        new_list.append(key) 
        new_list.append(val) 
 
    return new_list


newlist=create_list()

print(newlist)
