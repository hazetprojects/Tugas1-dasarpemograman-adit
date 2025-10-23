# Program menghitung gaji karyawan PT. DINGIN DAMAI

print("=== PT. DINGIN DAMAI ===")
print("PROGRAM HITUNG GAJI KARYAWAN KONTRAK")
print("-------------------------------")

# Gaji pokok
gaji_pokok = 300000

# Input data karyawan
nama = input("Masukkan nama karyawan: ")
golongan = int(input("Masukkan golongan (1/2/3): "))
pendidikan = input("Masukkan pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Masukkan jumlah jam kerja hari ini: "))

# Hitung tunjangan jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid!")

# Hitung tunjangan pendidikan
if pendidikan == "SMA":
 tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid!")

# Hitung honor lembur
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# Tampilkan hasil
print("\n=== RINCIAN GAJI KARYAWAN ===")
print(f"Nama Karyawan       : {nama}")
print(f"Golongan            : {golongan}")
print(f"Pendidikan          : {pendidikan}")
print(f"Jam Kerja           : {jam_kerja} jam")
print("-------------------------------")
print(f"Gaji Pokok          : Rp {gaji_pokok:,.0f}")
print(f"Tunjangan Jabatan   : Rp {tunjangan_jabatan:,.0f}")
print(f"Tunjangan Pendidikan : Rp {tunjangan_pendidikan:,.0f}")
print(f"Honor Lembur        : Rp {lembur:,.0f}")
print("-------------------------------")
print(f"Total Gaji          : Rp {total_gaji:,.0f}")
print("==============================")