def ubahKatas(masukan,ubahKata,gantiKata):
    return masukan.replace(ubahKata,gantiKata)
def hitungKata(kata,hitung):   
    return kata.count(hitung)
print("========== Program Manipulasi String ==========")
print(" Pilih Menu : ")
print("1. Hitung Kata")
print("2. Ubah Kata")
pilihan = int(input("Pilihan Anda : "))
if pilihan in (1,2):
    if pilihan == 2:
        masukan = input("Masukkan Sebuah Kalimat atau Kata : ")
        ubahKata = input("Masukan Kata yang ingi di ubah : ")
        gantiKata = input("Masukkan kata pengganti : ")
        print("String berhasil di ubah menjadi : ",ubahKatas(masukan,ubahKata,gantiKata))
    elif pilihan == 1:
        kata = input("Masukan sebuat kalimat/kata : ")
        hitung = input("Masukan Kata yang ingin di hitung : ")
        print("terdapat sebanyak",hitungKata(kata,hitung),hitung,"di dalam kalimat")
    else: print("Pilihan yang anda input tidak terdaftar di pilihan")
