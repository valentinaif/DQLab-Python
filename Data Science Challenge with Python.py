#TANTANGAN PEMROGRAMAN PYTHON

print("------Jumlah 7 Deret Pertama Fibonacci-----")

print("Tulislah sebuah fungsi Python yang digunakan untuk menghitung n deret pertama Fibonacci yang dimulai dari 0.")
#input = n : 7
#output = 33

print("-----Penyelesaian-----")

# Buat fungsi penjumlahan deret Fibonacci
def calculateSum(n):
    if n <= 0:
        return 0
    fibo = [0] * (n+1)
    fibo[1] = 1
    # Initialisasi hasil ke dalam variabel sm
    sm = fibo[0] + fibo[1]
    # Tambahkan suku-suku berikutnya
    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        sm += fibo[i]
    return sm
# Evaluasi hasil deret untuk n = 7    
print(calculateSum(7))