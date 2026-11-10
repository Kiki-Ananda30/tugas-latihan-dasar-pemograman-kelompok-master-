def total_harga(x, y) :
    return x * y

def transaksi(total_harga) :
    loop = True

    while loop :
        try :
            uang_pembayaran = int(input("Masukkan uang pembeli = "))
            loop = False
        except ValueError :
            print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")
            continue

    kembalian = uang_pembayaran - total_harga

    if uang_pembayaran < total_harga :
        print("Uang pembayaran kurang! transaksi batal.")
    else : 
        print(f"kembalian : Rp{kembalian:,.0f}")