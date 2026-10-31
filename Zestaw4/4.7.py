def flatten(sequence):
    flat = []
    for element in sequence:
        if isinstance(element, (list, tuple)):
            flat.extend(flatten(element))
        else:
            flat.append(element)
    return flat

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))   # [1,2,3,4,5,6,7,8,9]