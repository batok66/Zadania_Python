L = [[],[4],(1,2),[3,4],(5,6,7)]
S = []
for i in L:
    temp = 0
    for j in range(len(i)):
        temp += i[j]
    S.append(temp)
print("Lista list: " + str(L))
print("Suma elementów listy list: " + str(S))