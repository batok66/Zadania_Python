length = 0
miarka = ""
while True:
    length = input("Prosze podac liczbe naturalna: ")
    if length.isdigit():
        length = int(length)
        if length < 0 or length > 30:       # limit dlugosci 30 jednostek aby miescilo sie na ekranie
            print("Podano bledne dane.")
            continue
        break
    print("Podano bledne dane.")
    continue

miarka = miarka +("|")
for i in range(length):
    miarka = miarka + ("....|")
miarka = miarka + ("\t\n0")
for i in range(length):
    if i < 9:
        miarka = miarka + "    " + str(i + 1)
    else:
        miarka = miarka + "   " + str(i + 1)

print(miarka)