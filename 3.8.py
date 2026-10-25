sek1 = [1 , 2, 2, 3, 4]
sek2 = [1, 2, 3, 4, 5, 6, 7]

wspolne = []
bez_powtorzen = []

for i in range(len(sek1)):
    for j in range(len(sek2)):
        if sek1[i] == sek2[j]:
            wspolne.append(sek1[i])
wspolne.sort()
wspolne = list(set(wspolne))

bez_powtorzen = sek1 + sek2
bez_powtorzen.sort()
bez_powtorzen = list(set(bez_powtorzen))

print(wspolne)
print(bez_powtorzen)