def odwracanie_iteracyjnie(L, left, right):
    if left >= right:
        return L
    for i in range(int((right - left + 1) / 2)):
        tempL = L[left + i] ; tempR = L[right - i]
        L[left + i] = tempR ; L[right - i] = tempL
    return L

def odwracanie_rekurencyjne(L, left, right):
    if left >= right:
        return L
    tempL = L[left]
    tempR = L[right]
    L[left] = tempR ; L[right] = tempL
    return odwracanie_rekurencyjne(L, left + 1, right - 1)


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Oryginalny L: \t\t\t\t" + str(L))

L= odwracanie_iteracyjnie(L, 3, 7)
print("Po zmianie iteracyjnej: \t" + str(L))

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L= odwracanie_rekurencyjne(L, 3, 7)
print("Po zmianie rekurencyjnej: \t" + str(L))