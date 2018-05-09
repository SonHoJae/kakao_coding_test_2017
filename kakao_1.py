n = int(input())
if not (1<= n and n<=16):
    raise Exception("n range error")

arr1 = eval(input()) # list(map(int,input()))
arr2 = eval(input()) #list(map(int,input()))
answer = [0] * len(arr1)
for i in range(len(answer)):
    answer[i] = arr1[i] | arr2[i]
answer = list(map(bin,answer))

for idx, element in enumerate(answer):
    print(element)
    element = element[2:]
    element = element.replace('1','#')
    element = element.replace('0',' ')
    if len(element) < 6:
        element = (' ' * (6 - len(element))) + (element)
    answer[idx] = element
print(answer)

# 5
# [9,20,28,18,11]
# [30,1,21,17,28]

# 6
# [46, 33, 33 ,22, 31, 50]
# [27 ,56, 19, 14, 14, 10]