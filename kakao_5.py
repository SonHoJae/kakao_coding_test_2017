# str1 = input().lower()
# str2 = input().lower()

def multipleElements(s):
    result = []
    for i in range(len(s)-1):
        if not s[i].isalpha() or not s[i+1].isalpha():
            continue
        result.append(s[i]+s[i+1])
    return result
def union(str1,str2):
    d1 = dict()
    d2 = dict()
    count = 0
    for element in str1:
        if element in d1:
            d1[element] += 1
        else:
            d1[element] = 1
    for element in str2:
        if element in d2:
            d2[element] += 1
        else:
            d2[element] = 1

    for key in d1:
        if key in d2:
            count += max(d1[key], d2[key])
        else:
            count += d1[key]

    for key in d2:
        if key in d1:
            continue
        count += d2[key]
    return count

def intersection(str1,str2):
    d1 = dict()
    d2 = dict()
    count = 0
    for element in str1:
        if element in d1:
            d1[element] +=1
        else:
            d1[element] = 1
    for element in str2:
        if element in d2:
            d2[element] +=1
        else:
            d2[element] = 1
    for key in d1:
        if key in d2:
            count += min(d1[key], d2[key])
    return count


def jacardSimilarity(str1,str2):
    multiStr1 = multipleElements(str1)
    multiStr2 = multipleElements(str2)
    inter_count = intersection(multiStr1,multiStr2)
    union_count = union(multiStr1,multiStr2)
    try:
        result = 65536*(inter_count/union_count)
    except ZeroDivisionError:
        return 65536
    return result


print(int(jacardSimilarity('E=M*C^2'.lower(),'e=m*c^2'.lower())))