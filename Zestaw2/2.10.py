def amount(line):
    counter = 0
    for i in range(len(line)):
        if not line[i].isspace():
            if line[i - 1].isspace() or i == 0:
                counter += 1
    print(counter)

amount("Kot drzewo, piłka; słońce, \r\n książka.")
amount("")
amount("Pije sobie \nherabtkę.")
amount("    pozdrawiam")
amount("\twitam!")
