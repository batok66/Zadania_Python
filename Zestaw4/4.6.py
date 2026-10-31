def sum_seq(sequence):
    sum = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            sum += sum_seq(element)
        else:
            sum += element
    return sum

print(sum_seq([1, 2, 3]))
print(sum_seq((1, (2, 3), 4)))
print(sum_seq([1, [2, [3, 4]], 5]))
