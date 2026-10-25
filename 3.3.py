def petla_for():
    print("Liczby wypisane przy użyciu for: ")
    for i in range (31):
        if i % 3 != 0:
            print(i, end=" ")

def petla_while():
    print("\n\nLiczby wypisane przy użyciu while: ")
    i = 0
    while i < 31:
        if i % 3 != 0:
            print(i, end=" ")
        i += 1

petla_for()
petla_while()