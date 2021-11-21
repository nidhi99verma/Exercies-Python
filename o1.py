#factorial of numbers...ex:5--->1*2*3*4*5
def facto(nums):
    fact = 1
    for i in range(1, nums + 1):
        fact *= i
    return fact
print(facto(5))
   