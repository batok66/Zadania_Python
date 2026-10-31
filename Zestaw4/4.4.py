def fibbonacci(n):
    if n < 0:
        raise ValueError('n musi byc liczba naturalna.')
    if n == 0 or n == 1:
        return 1

    a = 1 ; wynik = 1
    for i in range(3, n):
        poprzedni = wynik
        wynik = a + wynik
        a = poprzedni
    return wynik

print(fibbonacci(10))