imie = input("podaj swoje imie: ")
print("witaj " + imie + "!")
print("oto bardzo prosty kalkulator")

x = int(input("podaj pierwszą cyfre całkowitą: "))
y = int(input("podaj drugą liczbe całkowitą: "))
z = str(input("podaj typ działania jaki chcesz zrobić z dwoma wypisanymi liczbami [np.: dodawanie]: "))

if z == "dodawanie":
    print(x + y)
elif z == "odejmowanie":
    print(x - y)
elif z == "mnożenie":
    print(x * y)
elif z == "dzielenie":
    print(x / y)
else:
    print("podano zły typ działania lub ten prgoram ssie")

print("Jak ci się podobał ten program?")
ocena = int(input("oceń w skali 1-10 :) "))

if ocena <= 4:
    print("aż tak źle?")
elif ocena > 10:
    print("dzięki za ocene poza skale")
elif ocena == 7 or ocena == 8 or ocena == 9:
    print("dzięki za wysoką ocenę :D")
else:
    print("i tak ten program pozostawia wiele do życzenia więc taka ocena jest sprawiedliwa")