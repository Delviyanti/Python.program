print("====================================================")
print("Selamat datang di layanan pemesanan tiket bioskop!")
print("====================================================")

genre_film = {
    "action": ["Fast and Furious", "John Wick"],
    "horor": ["Annabelle", "Pengabdi Setan", "The Nun 1", "The Nun 2", "The Conjuring", "Valak"],
    "comedy": ["Grown Ups", "The Hangover"],
    "anime": ["Naruto", "One Piece"],
    "drama": ["Titanic", "The Pursuit of Happyness"]
}

harga_tiket_biasa = 40000
harga_tiket_weekend = 45000

genre = input("Pilih genre (action, horor, comedy, anime, drama): ")
film = genre_film.get(genre)

if film:
    print("Berikut adalah pilihan film untuk genre", genre + ":")
    for i in range(len(film)):
        print(str(i+1) + ". " + film[i])
    
    pilihan = int(input("Pilih film (1-" + str(len(film)) + "): "))
    film_terpilih = film[pilihan-1]

    hari_list = ["1. Senin", "2. Selasa", "3. Rabu", "4. Kamis", "5. Jumat", "6. Sabtu", "7. Minggu"]
    print("\nSilakan pilih hari untuk menonton:")
    for hari in hari_list:
        print(hari)
    
    nomor_hari = int(input("Masukkan nomor hari (1-7): ")) - 1
    hari_terpilih = hari_list[nomor_hari]

    jumlah = int(input("Masukkan jumlah tiket: "))

    confirm = input("Beli atau tidak? (y/n): ")

    if confirm.lower() == 'y':
        nama = input("Masukkan nama: ")
        usia = int(input("Masukkan usia: "))

        if nomor_hari == 6:  # Cek apakah hari Minggu (nomor 6)
            harga_total = harga_tiket_weekend * jumlah
        else:
            harga_total = harga_tiket_biasa * jumlah

        print("\nDetail pemesanan:")
        print("1. Nama: ", nama)
        print("2. Umur: ", usia)
        print("3. Genre: ", genre)
        print("4. Film: ", film_terpilih)
        print("5. Harga: ", harga_total)
        print("6. Hari: ", hari_terpilih)
        print("\nTerima kasih telah menggunakan layanan pemesanan tiket bioskop kami.")
        print("Selamat menonton!")
    else:
        print("Pembelian dibatalkan.")
else:
    print("Genre tidak valid.")
