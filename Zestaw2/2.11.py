word = "literki rodzielone podkresleniem"

for i in range(len(word)):
    if i > 0:
        print("_", end="")
    print(word[i], end="")