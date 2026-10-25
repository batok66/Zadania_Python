while True:
    number = input("Prosze podac liczbe rzeczywista: ")
    if number == "stop":
        break
    try: float(number)
    except ValueError:
        print("Podano bledne dane. Prosze podac liczbe rzeczywista")
        continue
    print(number)
    number = float(number) ** 3
    print(number)
