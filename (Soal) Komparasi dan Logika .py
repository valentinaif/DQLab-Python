#LATIHAN SOAL KOMPARASI

print("_____SOAL NOMOR 1_____")

inputUser = float(input("masukan angka yang bernilai\nlebih dari 0\ndan\nkurang dari 5\natau\nlebih dari 8\ndan\nkurang dari 11\n:"))

#----------0++++++++++
#Memeriksa angka lebih dari 0
isLebihDari = (inputUser > 0)
print(isLebihDari)

#++++++++++5----------
#Memeriksa angka kurang dari 5
isKurangDari = (inputUser < 5)
print(isKurangDari)

#-------0+++++++5-------
#Memeriksa angka lebih dari 0 dan kurang dari 5
isCorrect = isLebihDari and isKurangDari

#----------8++++++++++
#Memeriksa angka lebih dari 8
isLebih = (inputUser > 8)
print(isLebih)

#++++++++++11----------
#Memeriksa angka kurang dari 11
isKurang = (inputUser < 11)
print(isKurang)

#-------8+++++++11-------
#Memeriksa angka lebih dari 8 dan kurang dari 11
isBenar = isLebih and isKurang

#-----0+++++5-----8+++++11-----
isAkhir = isCorrect or isBenar
print("(soal no 1)angka yang dimasukan = ", isAkhir)


print("\n",10*"=","\n")


print("_____SOAL NOMOR 2_____")

inputUser2 = float(input("masukan angka yang bernilai\nkurang dari 0\natau\nlebih dari 5\ndan\nkurang dari 8\natau\nlebih dari 11\n:"))

#++++++++++0-----
#Memeriksa angka kurang dari 0
Kurang = (inputUser2 < 0)
print(Kurang)

#-----5++++++++++
#Memeriksa angka lebih dari 5
LebihDari = (inputUser2 > 5)
print(LebihDari)

#++++++++++8-----
#Memeriksa angka kurang dari 8
KurangDari = (inputUser2 < 8)
print(KurangDari)

#-------5+++++8-------
#Memeriksa angka lebih dari 5 dan kurang dari 8
Correct = LebihDari and KurangDari

#-----11+++++++++++
#Memeriksa angka lebih dari 11
Lebih = (inputUser2 > 11)
print(Lebih)

#+++++0-----5+++++8-----11+++++
Akhir = Kurang or Correct or Lebih
print("(soal no 2) angka yang dimasukan = ", Akhir)