# Data diri disimpan ke dalam variabel
nama = "Muhammad Maulana Ramadhan"
umur = 18
tinggi = 163 #dalam cm
angka_favorit = 6

# Tampilkan data diri
print(f"Nama: {nama}")
print(f"Umur: {umur}")
print(f"Tinggi: {tinggi} cm")
print(f"Angka Favorit: {angka_favorit}")


# Hitung total harga belanja di toko alat tulis
harga_pensil_per_buah = 2000
jumlah_pensil = 4
harga_buku_per_buah = 5000
jumlah_buku = 2

total_harga_pensil = jumlah_pensil * harga_pensil_per_buah
total_harga_buku = jumlah_buku * harga_buku_per_buah
total_belanja = total_harga_pensil + total_harga_buku

# Tampilkan total belanja di toko alat tulis
print(f"Total Harga Pensil: Rp{total_harga_pensil}")
print(f"Total Harga Buku: Rp{total_harga_buku}")
print(f"Total Harga Belanja: Rp{total_belanja}")


# Tampilkan angka favorit
if angka_favorit % 2 == 0:
 print(f"Angka favorit {angka_favorit} adalah angka genap")