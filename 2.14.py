line = ("slowo dlugieslowo bardzodlugieslowo")

if len(line) == 0:
    print("String line jest pusty.")

else:
    sorted_line = sorted(line.split(), key=len)

    length = 0
    for i in sorted_line[len(sorted_line) - 1]:
        length += 1

    print("Line: \t" + line)
    print("Najdluzsze slowo: " + sorted_line[len(sorted_line)-1])
    print("Dlugosc najdluzszego slowa: " + str(length))

