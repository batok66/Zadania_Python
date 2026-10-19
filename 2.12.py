line = "ksiazka kubek myszka lampka Kwiatek półka"
newF = ""
newL = ""

print("String line: " + line)

if line[0].isalpha():
    newF = line[0]

for i in range(len(line)):
    if line[i].isalpha():
        if line[i - 1].isspace():
            newF = newF + line[i]
print("Wyraz z pierwszych liter: " + newF)

for i in range(len(line)):
    if line[i].isalpha():
        if i != len(line) - 1:
            if line[i + 1].isspace():
                newL = newL + line[i]
        else:
            newL = newL + line[i]

print("Wyraz z ostatnich liter: " + newL)
