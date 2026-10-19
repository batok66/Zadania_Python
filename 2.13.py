line = "ksiazka kubek"
counter = 0

for i in range(len(line)):
    if not line[i].isspace():
        counter += 1

print("Line: " + line)
print("Ilość liter = " + str(counter))