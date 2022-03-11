import math

x = int(input("Podaj liczbe którą chcesz spierwiastkować: "))
if x < 0:
    print("BŁĄD. Liczb ujemnych nie da sie pierwiastkować.")
else:
    print("Wynik pierwiastkowania wwnosi: ",math.sqrt(x))