# -*- coding: utf-8 -*-
"""Pengenalan Fungsi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KOZX8jkT68PzRzi54zHko2av2qXrDJCn
"""





# Deklarasikan list buku
buku = []

# Fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")  # Menggunakan tanda kurung pada print
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")  # Menggunakan f-string untuk print lebih mudah

# Fungsi untuk menambah data
def insert_data():
    buku_baru = input("Judul Buku: ")  # Menggunakan input
    buku.append(buku_baru)

# Fungsi untuk edit data
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))  # Mengubah input menjadi int
        if indeks >= len(buku) or indeks < 0:  # Ubah kondisi untuk memeriksa indeks
            print("ID salah")  # Tambahkan tanda kurung pada print
        else:
            judul_baru = input("Judul baru: ")  # raw_input diubah menjadi input
            buku[indeks] = judul_baru
    except ValueError:
        print("Input ID harus berupa angka.")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))  # Mengubah input menjadi int
        if indeks >= len(buku) or indeks < 0:  # Gunakan '>=', karena indeks dimulai dari 0
            print("ID salah")  # Tambahkan tanda kurung pada print
        else:
            buku.remove(buku[indeks])  # Menghapus item berdasarkan indeks
    except ValueError:
        print("Input ID harus berupa angka.")

# Fungsi untuk menampilkan menu
def show_menu():
    print("\n")
    print("----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    try:
        menu = int(input("PILIH MENU> "))  # Mengubah input menjadi int
        print("\n")

        if menu == 1:
            show_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            print("Program selesai.")
            return False  # Menggunakan return False untuk mengakhiri loop
        else:
            print("Salah pilih!")  # Tambahkan tanda kurung pada print
    except ValueError:
        print("Input menu harus berupa angka.")

    return True  # Loop akan terus berlanjut jika tidak memilih exit

if __name__ == "__main__":
    running = True
    while running:
        running = show_menu()

# Membuat Fungsi
def salam():
    print("Hello, Selamat Pagi")  # Perbaikan penggunaan print pada Python 3

# Pemanggilan Fungsi
salam()

# Membuat Fungsi
def salam():
    print("Hello, Selamat Pagi")  # Perbaikan penggunaan print pada Python 3

# Pemanggilan Fungsi
salam()
salam()
salam()

# Membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print("Luas segitiga: %f" % luas)  # Perbaikan print untuk Python 3

# Pemanggilan fungsi
luas_segitiga(4, 6)

# Membuat fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# Pemanggilan fungsi
print("Luas persegi: %d" % luas_persegi(6))  # Perbaikan penggunaan print di Python 3

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume  # Tambahkan return untuk mengembalikan nilai volume

# Membuat variabel global
nama = "Desky "
versi = "1.0.0"

def help():
    # Ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # Mengakses variabel lokal
    print("Nama: %s" % nama)
    print("Versi: %s" % versi)

# Mengakses variabel global
print("Nama: %s" % nama)
print("Versi: %s" % versi)

# Memanggil fungsi help()
help()