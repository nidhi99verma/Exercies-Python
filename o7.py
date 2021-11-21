#   *  
#  *** 
# ***** print

def print_t(n):
    x = '*'
    y = ' '
    z = n-1
    for i in range(1,n+1):
        print(f"{y*(z)}{x}{y*(z)}")
        z-=1
        x += "**"
    return     
print_t(3)    
