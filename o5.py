#make a function that revers string and index of given list
def string_index_revers(lists):
    rev_list = []
    for i in lists:
        rev_list.append(i[::-1])
    return rev_list[::-1]  
print(string_index_revers(['Nidhi','Ajai','Veram']))      
