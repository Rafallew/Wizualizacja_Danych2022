lista_parzystych_liczb = []
i = 0
while i <= 9:
    x = int(input("Wprować liczbe: "))
    if x % 2 == 0:
        lista_parzystych_liczb.append(x)
    i += 1
print("To są wszystkie liczby parzyste które zostały podane: ",lista_parzystych_liczb)