def total_harga(x, y) :
    return x * y

def transaksi(total_harga) :
    loop = True

    while loop :
        try :
            uang_pembayaran = int(input("Masukkan uang pembeli = "))

            while uang_pembayaran < total_harga :
               print("Uang pembayaran kurang!")
               is_lanjut = input("Lanjut? [y/n] : ").lower()

               if is_lanjut == 'y' :
                   uang_pembayaran = int(input("Masukkan uang pembeli = "))
                   if uang_pembayaran >= total_harga :
                       break                    
               elif is_lanjut == 'n':
                    break
               else : 
                   print("Input tidak valid! Coba lagi.")
                   continue

            kembalian = uang_pembayaran - total_harga
            if kembalian < 0 :
                print("Transaksi batal.")
            else :
                print(f"kembalian : Rp{kembalian:,.0f}")
                
            loop = False
        except ValueError :
            print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")
            continue

    