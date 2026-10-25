# 1.
L = [3, 5, 4]
# L = L.sort()  #sort() nie zwraca niczego, na ekran drukuje się "None"
L.sort()        # poprawnie sortowanie w miejscu

# 2.
#x, y = 1, 2, 3  # ValueError: too many values to unpack (expected 2), zbyt dużo literałów do przypsiania
x, y = 1, 2      # poprawnie

# 3.
X = 1, 2, 3
# X[1] = 4       # TypeError: 'tuple' object does not support item assignment
                 # tupla jest niemodyfikowalana, przypisanie wywoluje błąd

# 4.
X = [1, 2, 3]
# X[3] = 4       # IndexError: list assignment index out of range
                 # lista indexowana od 0, przypisanie czegos do pozycji 3 wykracza poza zakres listy

# 5.
X = "abc"
# X.append("d")  # AttributeError: 'str' object has no attribute 'append'
                 # metoda append() nie działa dla stringów, działa na listach
X = X + "d"      # poprawnie

# 6.
#L = list(map(pow, range(8))) # TypeError: pow() missing required argument 'exp' (pos 2)
                 # pow() wymaga dwoch argumentow, powyżej przekazano tylko jeden

L = list(map(pow, range(8), range(8))) # poprawnie 


