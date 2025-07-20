# Zadanie 3: Konwersja temperatury ze stopni Fahrenhaita na stopnie Celcjusza,
# Konwersja temperatury ze stopni Fahrenheinta na stopnie Kelvina
# Zainicjalizuj temp w Farh
# Zainicjalizuj temp w Celcjuszach jako nowa zmienna np: temp_cel i przypisz do niej wynik konwersji 
# Zainicjalizuj temp w Kelwinach jako nowa zmienna np: temp_kel i przypisz do niej wynik konwersji
# Temperatura wejsciowa w Fahrenhaicie powinna byc wczytana przez uzytkownika 

print("Zadanie 3: Konwersja temperatury ze stopni Fahrenheita na stopnie Celcjusza i Kelvina")
kelvin_offset = 273.15          # Stała do konwersji z Celsjusza na Kelvina
fahrenheit_to_celsius = 5 / 9   # Współczynnik konwersji z Fahrenheita na Celsjusza
fahrenheit_constant = 32        # Stała do konwersji z Fahrenheita na Celsjusza

temp_fahr = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
print("Temperatura w Fahrenheicie:", temp_fahr)

temp_cel = (temp_fahr - fahrenheit_constant) * fahrenheit_to_celsius
print("Temperatura w Celsjuszach:", temp_cel)

temp_kel = temp_cel + kelvin_offset
print("Temperatura w Kelvinach:", temp_kel)