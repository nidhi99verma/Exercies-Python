def count_str(sub, strs):
    count = 0
    strLen = len(strs)
    for i in range(strLen):
        status = True
        inc = 0
        for j in range(len(sub)):
            if (i == strLen):
                status = False
                break
            elif strs[i] == sub[j]:
                i += 1
                inc += 1
            else:
                status = False
                break
        if (status == False):
            i -= inc
        else:
            count += 1
    
    return count
print(count_str("c","bca bc a bca nbcd bc"))                    