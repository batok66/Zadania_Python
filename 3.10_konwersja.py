# implementacja funkcji roman2int() do konwersji rzymskiej na arabska

rzymskie = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def roman2int(liczba):
    aktualna = 0
    if len(liczba) == 0:
        return 0
    for i in range(len(liczba)):
        if i + 1 < len(liczba) and rzymskie[liczba[i]] < rzymskie[liczba[i + 1]]:
            aktualna -= rzymskie[liczba[i]]
        else:
            aktualna += rzymskie[liczba[i]]
    return aktualna

print(roman2int('MMCDLIV'))
print(roman2int('MMMCMXCIX'))
print(roman2int('MMXXVI'))
print(roman2int('MMMDCCCLXXXVIII'))
print(roman2int('MCMIV'))