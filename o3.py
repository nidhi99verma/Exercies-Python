#make a function that find index value of item , whose value sum is equal to target value..ex->l=[1,2,3,5],8.....output:2,3
def f_l(l,t):
    new = []
    for i in l:
        for j in l:
            if i == j:
                break
            if (i + j == t):
                new.append(l.index(j))
                new.append(l.index(i))    
    return new
print(f_l([3,2,4,5,8],6))            
