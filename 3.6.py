def wymiar():
    while True:
        liczba = input()
        if liczba.isdigit():
            liczba = int(liczba)
            if liczba < 1 or liczba > 30:
                print("Podano bledne dane.")
                continue
            return liczba
        print("Podano bledne dane.")
        continue

print("Prosze podac szerokosc prostokata: ")
x = wymiar()
print("Prosze podac wysokosc prostokata: ")
y = wymiar()

prostokat = ""

for i in range(y):
    prostokat += "+---" * x + "+\n"
    prostokat += "|   " * x + "|\n"

prostokat += "+---" * x + "+\n"

print(prostokat)