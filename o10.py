#sort list without sort function
def short(*args):
    lists = []
    for j in range(0,max(args)+1):
        for i in args:
            if j == i:
                lists.append(i)
    return lists
#print(short(7,3,4,8,9,1,2,5))                
#
def shorts(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if i == j:
                continue
            if alist[i] < alist[j]:
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp
    return alist
alist = [3,5,1,9,4,6,8,2]
print(shorts(alist))    

#
def shor(list_n):
    new = []
    for i in range(len(list_n)):
        new.append(min(list_n))
        list_n.remove(min(list_n))
    return new 
list_n = [7,3,4,8,9,1,2,5]    
#print(shor(list_n))                   