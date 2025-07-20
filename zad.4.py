print('Oblicz zysk z konta oszczędnościowego')

kwota = float(input('Podaj kwotę: '))
oprocentowanie = float(input('Podaj oprocentowanie w %: '))
lata = float(input('Podaj liczbę lat: '))

zysk = kwota * (1 + oprocentowanie / 100) ** lata - kwota

# Zaokrąglamy wynik do 2 miejsc po przecinku
print("Zysk po", lata, "latach wynosi", round(zysk, 2)) 