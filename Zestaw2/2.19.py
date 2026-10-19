L = [1, 2, 3, 12, 23, 44, 100, 524, 662]
string = ""

for item in L:
    temp= str(item)
    temp = temp.zfill(3)
    string += temp

print(string)
