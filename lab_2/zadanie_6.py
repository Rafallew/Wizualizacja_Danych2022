def liczby(a, b, c):

   if (a == b and b == c):

       return 'Wszystkie liczby  sa rowne, każda z nich ma wartość:', a

   elif (a>=b):
       if a > c:
           print("Liczba 'a' jest największa i wynosi: ",a)
       else:
           print("Liczba 'c' jest największa i wynosi: ",c)
   elif b > a:
       if b > c:
           print("Liczba 'b' jest największa i wynosi: ",b)
       else:
           print("Liczba 'c' jest największa i wynosi: ",c)

a = int (input("podaj liczbe 'a': "))
b = int (input("podaj liczbe 'b': "))
c = int (input("podaj liczbe 'c': "))

print(liczby(a, b, c))