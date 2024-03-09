import ast

def extract_names_to_list(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

def extract_three_names_to_list(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter+=1
    return L

def extract_director_names_to_list(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

def remove_spaces(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1