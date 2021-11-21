#a = 5, b = 7....b-a=2
#number swip 
def swip(a,b):
    
    if a < b:
        c = b - a
        b = b - c
        a = c + a   
    elif b < c:
        c = a - b 
        a = a - c
        b = c + b
    else:
        a = b    
    return (a,b)
print(swip(10,25))        
#--
def sw(x,y):
    if x != y:
       z = x
       x = y
       y = z
    return(x,y)
print(sw(2,3))    