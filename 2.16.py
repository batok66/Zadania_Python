line1 =  "W tekście znajdującym się w stringu line zamienić ciąg znaków 'GvR' na 'Guido van Rossum'."
line2 = "GvR witam GvR"

new1 = line1.replace("GvR", "Guido van Rossum")
new2 = line2.replace("GvR", "Guido van Rossum")

print("Oryginal: \t" + line1)
print("Po zmianie:\t" + new1)

print("Oryginal: \t" + line2)
print("Po zmianie:\t" + new2)