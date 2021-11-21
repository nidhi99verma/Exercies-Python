#    *  
#   ***  
#  *****
# ********     <----print
#  *****
#   ***
#    *
  
def print_t(n):
    x = '*'
    y = ' '
    z = n-1
    c = 0
    for i in range(0,n-1):
        print(f"{y*(z)}{x}{y*(z)}")
        z-=1
        x += "**"
    x = '*'
    y = ' '
    z = n - 1
    c = 0
    for j in range(0,n):
        print(f"{y*(c)}{x*(n + z)}{y*(c)}")
        z -= 2
        c +=1
    return     
print_t(4)    
