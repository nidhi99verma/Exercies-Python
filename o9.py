#sort list with limit
def short(*args):
    lists = []
    for j in range(0,max(args)+1):
        for i in args:
            if j == i:
                lists.append(i)
    return lists

def sort_item(num1,*argss):
    listsn = []
    for i in argss:
        if i <= num1:
            listsn.append(i)
            listsn.short()
    return listsn 
print(sort_item(33,9,1,23,3,33,67,8))            