 #find target in given list given by user
def find_ind(list_num,target):
    list_index = 0
    for i in list_num:
        if (i == target):
            return list_index
        list_index += 1

print(find_ind([2,3,4,5,6,7,9],7))                