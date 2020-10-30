# DDP LAB-3
print ("\t" * 2, "|========================================|")
print ("\t" * 2, "|      SELAMAT DATANG DI MENU PEKAN 4    |")
print ("\t" * 2, "|========================================|")
def hitung():
    print("\t" * 2, "\n Silahkan pilih luas yang ingin dihitung!")  
    print("\t" * 2, "========================================")
    print("\t" * 2, "1. Permainan Gunting Kertas Batu")
    print("\t" * 2, "2. Toko Buku Bekas")
    print("\t" * 2, "3. Membuat Persegi")
    print("\t" * 2, "========================================")
    print("\t" * 2, "Silahkan pilih 1-3")
    print('')

    pilih = input("Masukkan pilihan: ")

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
    if pilih == '1':
      print("\t" * 4 ,"Permainan Gunting, Batu, Kertas")
      print("\t" * 3 , "=" * 39)

      p1 = input("Player-1 masukan pilihan anda (gunting/batu/kertas) : ")
      p2 = input("Player-2 masukan pilihan anda (gunting/batu/kertas) : ")

      if p1 == p2:
        print("\nPertandingan Seimbang")

      elif p1 == "gunting":
        if p2 == "batu":
          print("\nPlayer-2 Menang")
        elif p2 == "kertas":
          print("\nPlayer-1 Menang")
        else:
          print("\nPlayer-2 belum memasukan pilihan")

      elif p1 == "batu":
        if p2 == "kertas":
          print("\nPlayer-2 Menang")
        elif p2 == "gunting":
          print("\nPlayer-1 Menang")
        else:
          print("\nPlayer-2 belum memasukan pilihan")

      elif p1 == "kertas":
        if p2 == "gunting":
          print("\nPlayer-2 Menang")
        elif p2 == "batu":
          print("\nPlayer-1 Menang")
        else:
          print("\nPlayer-2 belum memasukan pilihan")

      else:
        print("\nPlayer-1 belum memasukan pilihan atau masukan salah")

      tanya()

# SOAL 2 - Toko Buku Bekas
# Tuliskan program untuk Soal 2 di bawah ini
    if pilih == '2':
      print("\n\n")
      print("\t" * 6 ,"Toko Buku Bekas")
      print("\t" * 3 , "=" * 39)

      b_buku = int(input("Masukan banyaknya buku yang akan dibeli : "))
      if b_buku <= 10:
        bayar = b_buku * 20000
        print("Harga yang harus dibayar %d rupiah" % bayar)

      elif b_buku == 11 or b_buku <= 25:
        bayar = b_buku * 18000
        print("Harga yang harus dibayar %d rupiah" % bayar)

      elif b_buku == 26 or b_buku <= 50:
        bayar = b_buku * 15000
        print("Harga yang harus dibayar %d rupiah" % bayar)

      elif b_buku >50:
        bayar = b_buku * 10000
        print("Harga yang harus dibayar %d rupiah" % bayar)
      
      tanya()
        
#  SOAL 3 - Mencetak Persegi
# Tuliskan program untuk Soal 3 di bawah ini
    if pilih == '3':
      print("\n\n")
      print("\t" * 6 ,"Mencetak Persegi")
      print("\t" * 3 , "=" * 39)

      b_bulat = int(input("Masukan sebuah bilangan bulat : "))

      for i in range(b_bulat):
        for j in range(b_bulat):
          if i % 2 == 0:
            print('#', end=' ')
          else:
            print('$', end=' ')
        print()

      tanya()


def tanya():
    tanya = input('\n\tKembali ke menu (y/t)?')
    if tanya == 'y':
        hitung()
    elif tanya == 't':
        print("\nTerima kasih")
    else:
        print('\n\tPilihan tidak ada !!!')

hitung()
