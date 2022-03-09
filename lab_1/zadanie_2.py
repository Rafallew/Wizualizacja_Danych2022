print('KALKULATOR')
print('Co chcesz zrobić?')
print('Dodawanie wybierz: 1')
print('Odejmowanie wybierz: 2')
print('Mnożenie wybierz: 3')
print('Dzielenie wybierz: 4')


a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))

dzialanie = input('Wybierz działanie: ')
if dzialanie == '1':
    wynik = a + b
elif dzialanie == '2':
    wynik = a - b
elif dzialanie == '3':
    wynik = a * b
elif dzialanie == '4':
    wynik = a / b
else:
    wynik = 'Nie ma takiego działania, spróbuj jeszcze raz.'

print(wynik)