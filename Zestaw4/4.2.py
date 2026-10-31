def make_ruler(n):
    if n <= 0:
        raise ValueError('n musi byc liczba naturalna.')
    miarka = ""
    miarka = miarka +("|")
    for i in range(n):
        miarka = miarka + ("....|")
    miarka = miarka + ("\t\n0")
    for i in range(n):
        if i < 9:
            miarka = miarka + "    " + str(i + 1)
        else:
            miarka = miarka + "   " + str(i + 1)

    return miarka

def make_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        raise ValueError('rows oraz cols musi byc liczba naturalna.')
    prostokat = ""
    for i in range(rows):
        prostokat += "+---" * cols + "+\n"
        prostokat += "|   " * cols + "|\n"
    prostokat += "+---" * cols + "+\n"

    return prostokat

print(make_ruler(10))
print("\n")
print(make_grid(2,4))