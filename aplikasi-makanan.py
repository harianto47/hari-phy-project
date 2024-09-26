
import os
os.system('cls')

#function untuk cetak menu
def darfar_menu():
    print("=MENU PILIHAN=")
    print("==============")
    print("1.  BAKSO    ")
    print("2.  MIE AYAM ")
    print("==============")    

#function untuk membuat format uang indonesia   
def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return 'Rp'+' '+ y     
    else :
        p = y[-3:]
        q = y[:-3]
        return   formatrupiah(q) + '.' + p
    

#dictionary
menu={
    '1':'BAKSO',
    '2':'MIE AYAM'
}
harga={
    '1' : 10000,
    '2' : 15000
}

#perulangan
pilihan="y"
while pilihan == "y":
    os.system("cls")
    darfar_menu()

    a = input("MASUKAN PILIHAN  = ")

    if  a in menu:# cari nilai a di menu
        print(f"PILIHAN ANDA -----> {menu[a]}")
        b = input("JUMLAH ORDER     = ")
        if b.isnumeric(): # b adalah number
            print("")
            c=input("APAKAH PILIHAN dan ORDER SUDAH SESUAI --> y/n=")
            c.lower()
            if c == "y": #jika c bernilai variable "y"
                os.system("cls")
                b=int(b)
                d= harga[a]*b
                print("====================================")
                print("DETAIL PEMBELIAN")
                print("====================================")
                print(f"MENU Di PILIH    = {menu[a]}")
                print(f"HARGA            = {formatrupiah(harga[a])}")
                print(f"BANYAKNYA PESAN  = {b}")
                print(f"TOTAL HARGA      = {formatrupiah(d)}")
                print("====================================")
            else:
                os.system("cls")
                continue
                  
        else:
            print("")
            print("JUMLAH ORDER HANYA BOLEH INPUT ANGKA")
    else:
        print("")
        print("MENU TIDAK TERSEDIA")

    print("")
    pilihan=input("APAKAH MAU ORDER LAGI? y/n    = ")


        