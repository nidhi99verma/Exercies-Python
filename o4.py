# math.ceil(number)(ex:2.3->3,4.6->5),math.floor(number)(ex:2.3->2,4.6->4)
#make a function that give output in deducted % value by given item...% depend upon number range(ex:1-10->1%,11-20->2%.....990-1000->100%)
import math
def per_incr(num):
    after_mp = ''
    p = math.ceil(num/10)
    after_mp = num -((num*p)/100)
    return after_mp
print(per_incr(100))          