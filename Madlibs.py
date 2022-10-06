#Cara menggabungkan string

print("=====PERTAMA=====")

#Jika ingin membuat string seperti "subscribe to _____"

youtuber = "RANS Entertaiment" #beberapa variabel string

#Beberapa cara untuk melakukannya
print("subscribe to " + youtuber)
print("subscribe to {}". format(youtuber))
print(f"subscribe to {youtuber}")

print("\n=====KEDUA=====")

adj = input("Adjective : ")
verb1 = input("Verb1 : ")
verb2 = input("Verb2 : ")
cita_cita = input("Cita_cita : ")

madlibs = f"Belajar program {adj} membuat saya bersemangat sepanjang waktu karena aku sangat cinta {verb1}. Terus tingkatkan skill dan {verb2} sampai bisa menjadi seorang {cita_cita}!."
print(madlibs)