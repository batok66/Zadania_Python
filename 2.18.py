number = 1020300023020 #liczba zer to 7 
counter = 0

string = str(number)

for i in range(len(string)):
    if string[i] == "0":
        counter += 1

print(counter)