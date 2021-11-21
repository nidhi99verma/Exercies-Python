#min function
def shorts(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if i == j:
                continue
            if alist[i] < alist[j]:
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp
    return alist[0]
alist = [3,5,1,9,4,6,8,2]
print(shorts(alist))

#max function
def short(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            if i == j:
                continue
            if alist[i] < alist[j]:
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp
    return alist[-1]
alist = [3,5,1,9,4,6,8,2]
print(short(alist))