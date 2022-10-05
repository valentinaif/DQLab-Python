#Latihan Konversi Temperatur

print("=====NOMOR 1=====")

#Program konversi fahrenheit ke satuan lain

print("\nProgram Konversi Temperatur Fahrenheit\n")

fahrenheit1 = float(input("Masukan suhu dalam fahrenheit = "))
print("suhu adalah", fahrenheit1, "fahrenheit")

#Celcius
celcius1 = (5/9)*(fahrenheit1 - 32)
print("suhu dalam celcius adalah", celcius1, "celcius")

#Reamur
reamur1 = (4/9)*(fahrenheit1 - 32)
print("suhu dalam reamur adalah", reamur1, "reamur")

#Kelvin
kelvin1 = celcius1 + 273
print("suhu dalam kelvin adalah", kelvin1, "kelvin")

print("\n=====NOMOR 2=====\n")

#Program konversi kelvin ke satuan lain

print("\nProgram Konversi Temperatur Kelvin\n")

kelvin2 = float(input("Masukan suhu dalam kelvin = "))
print("suhu adalah", kelvin2, "kelvin")

#Celcius
celcius2 = kelvin2 - 273
print("suhu dalam celcius adalah", celcius2, "celcius")

#Reamur
reamur2 = (4/9)*(kelvin2 - 273)
print("suhu dalam reamur adalah", reamur2, "reamur")

#Fahrenheit
fahrenheit2 = ((9/5) * celcius2) + 32
print("suhu dalam fahrenheit adalah", fahrenheit2, "fahrenheit")