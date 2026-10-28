from total_pembelian import total_harga

print("=========== Laundry Kiloan FrameKita ==========")
print("""\t\t--- Menu ---
1. Cuci kering           : Rp 6.000/kg
2. Cuci kering + Setrika : Rp 8.000/kg
3. Cuci satuan           : Rp 5.000/pcs
4. Setrika saja          : Rp 4.000/kg
5. Cuci sepatu           : Rp 20.000/pasang
6. Cuci tas              : Rp 15.000/pcs
7. Cuci Bed cover        : Rp 25.000/pcs
8. Cuci kilat            : Rp 12.000/kg
9. Keluar/Selesai""")

program_berjalan = True
list_total = []

while program_berjalan :
    namaPelanggan = input("Masukkan nama anda : ")
    if not namaPelanggan.strip() :
        print("Nama harus diisi!")
    else :
        break

while namaPelanggan : 
    inputPelanggan = int(input("\nMasukkan pilihan anda (1-9) : "))
    if inputPelanggan < 1 or inputPelanggan > 9:
        print("Pilihan tidak valid. Masukkan angka 1-9.")

    match inputPelanggan :
        case 1 :
            harga = 6000
            loop = True
            print("-------------------------")
            print("Cuci kering : Rp 6.000/kg")
            print("-------------------------")
            while loop :
                try :
                    berat_cucian = float(input("Masukkan berat cucian : "))
                    if float(berat_cucian) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")
                
                list_total.append(total_harga(harga, berat_cucian))
        case 2 :
            harga = 8000
            loop = True
            print("-----------------------------------")
            print("Cuci kering + Setrika : Rp 8.000/kg")
            print("-----------------------------------")
            while loop :
                try :
                    berat_cucian = float(input("Masukkan berat cucian : "))
                    if float(berat_cucian) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")

                list_total.append(total_harga(harga, berat_cucian))
        case 3 :
            harga = 5000
            loop = True
            print("------------------------------------")
            print("Cuci satuan           : Rp 5.000/pcs")
            print("------------------------------------")
            while loop :
                try :
                    pakaian = str(input("Masukkan pakaian yg dicuci : "))
                    if str(pakaian) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")

                list_total.append(total_harga(harga, 1))
        case 4 :
            harga = 4000
            loop = True
            print("-----------------------------------")
            print("Setrika saja          : Rp 4.000/kg")
            print("-----------------------------------")
            while loop :
                try :
                    berat = float(input("Masukkan berat : "))
                    if float(berat) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")

                list_total.append(total_harga(harga, berat))
        case 5 :
            harga = 20000
            loop = True
            print("----------------------------------------")
            print("Cuci sepatu           : Rp 20.000/pasang")
            print("----------------------------------------")
            while loop :
                try :
                    sepatu = float(input("Masukkan berapa pasang sepatu : "))
                    if float(sepatu) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")

                list_total.append(total_harga(harga, sepatu))
        case 6 :
            harga = 15000
            loop = True
            print("-------------------------------------")
            print("Cuci tas              : Rp 15.000/pcs")
            print("-------------------------------------")
            while loop :
                try :
                    tas = int(input("Masukkan berapa banyak tas : "))
                    if int(tas) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")

                list_total.append(total_harga(harga, tas))
        case 7 :
            harga = 25000
            loop = True
            print("-------------------------------------")
            print("Cuci Bed cover        : Rp 25.000/pcs")
            print("-------------------------------------")
            while loop :
                try :
                    bed_cover = int(input("Masukkan berapa banyak bed cover : "))
                    if int(bed_cover) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")

                list_total.append(total_harga(harga, bed_cover))
        case 8 :
            harga = 12000
            loop = True
            print("------------------------------------")
            print("Cuci kilat            : Rp 12.000/kg")
            print("------------------------------------")
            while loop :
                try :
                    berat_cucian = float(input("Masukkan berat cucian : "))
                    if float(berat_cucian) :
                        loop = False                
                except ValueError :
                    print("ValueError: Input yang dimasukkan tidak valid! Coba lagi.")
                list_total.append(total_harga(harga, berat_cucian))
        case 9 :
                sum = 0
                for i in list_total:      
                    sum += i
                print(f"Total Semua : Rp{sum:,.0f}") 
                break