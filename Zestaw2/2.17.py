line = "Posortować wyrazy ze stringu line raz alfabetycznie, a raz pod względem długości."

alphabetically = sorted(line.split(), key=str.lower)
bylength = sorted(alphabetically, key=len)

print(line)
print(alphabetically)
print(bylength)