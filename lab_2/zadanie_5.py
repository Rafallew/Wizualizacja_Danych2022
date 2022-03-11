import sys

def pobiez_liczbe_od_urzytkownika():
    while True:
        dane_urzytkownika = sys.stdin.readline()
        try:
            wartosc = float(dane_urzytkownika)
            return wartosc
        except ValueError:
            print("BŁĄD. Wprowadź ponownie liczbę")


sys.stdout.write("Wprowadź liczbę a: ")
a = pobiez_liczbe_od_urzytkownika()
sys.stdout.write("Wprowadź liczbę b: ")
b = pobiez_liczbe_od_urzytkownika()
sys.stdout.write("Wprowadź liczbę c: ")
c = pobiez_liczbe_od_urzytkownika()
sys.stdout.write("a^b + c = %.4f" % ((a ** b) + c))