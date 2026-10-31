def factorial(n):
    if n < 0:
        raise ValueError('n musi byc liczba naturalna.')
    wynik = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

print(factorial(4))
print(factorial(5))
print(factorial(6))