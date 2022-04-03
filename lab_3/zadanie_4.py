a = int(input("Wprowadz przyprostokątną: a "))
b = int(input("Wprowadz przyprostokątną: b "))
c = int(input("Wprowadz przyprostokątną: c "))

if ((a + b > c) and (b + c > a) and (c + a > b)):
    if((a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (c**2 + a**2 == b**2)):
        print("Trójkąt  jest prostokątny")
    else:
        print("Trójkąt nie jest prostokątny")
else:
    print("Błędnie dane. To nie jest trójkąt" )