def create_an_empty_list():
    return []

def create_a_list():
    mylist = create_an_empty_list()
    mylist.append(1)
    mylist.append("2 fish")
    mylist.append([3, "cows"])
    mylist.append("4 cats")
    return mylist

def add_element_to_end_of_list(l, element):
    # l = create_a_list()
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    # l=create_a_list()
    l.insert(0,element)
    return l

def remove_element_from_end_of_list(l):
    # l= create_a_list()
    l.pop()
    return l

def remove_element_from_start_of_list(l):
    del l[0]
    return l

def retrieve_first_element_from_list(l):
    x=l[0]
    return x

def retrieve_element_from_index(l, index):
    x=l[index]
    return x

def retrieve_last_element_from_list(l):
    x=l[-1]
    return x
