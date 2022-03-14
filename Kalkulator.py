print("KALKULATOR SEDERHANA\n")
print("""1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian""")

n = int(input("\nMasukan Pilihan : "))
num1 = int(input("Masukan Angka-1 : "))
num2 = int(input("Masukan Angka-2 : "))
if n == 1 :
    c = num1 + num2
    print("Hasilnya :", c)
elif n == 2 :
    c = num1 - num2
    print("Hasilnya :", c)
elif n == 3 :
    c = num1 * num2
    print("Hasilnya :", c)
elif n == 4 :
    c = num1 / num2
    print("Hasilnya :", c)
else :
    print("Input Salah")