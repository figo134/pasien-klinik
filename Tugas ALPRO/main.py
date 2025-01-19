class Pasien:
    def __init__(self, nama, no_antrian):
        self.nama = nama
        self.no_antrian = no_antrian

    def __str__(self):
        return f"No. Antrian: {self.no_antrian}, Nama: {self.nama}"

class Klinik:
    def __init__(self):
        self.antrian = []

    def daftar_pasien(self, nama):
        no_antrian = len(self.antrian) + 1
        pasien = Pasien(nama, no_antrian)
        self.antrian.append(pasien)
        print(f"Pasien {nama} terdaftar dengan nomor antrian {no_antrian}.")

    def panggil_pasien(self):
        if self.antrian:
            pasien = self.antrian.pop(0)
            print(f"Memanggil pasien: {pasien.nama} (No. Antrian: {pasien.no_antrian})")
        else:
            print("Tidak ada pasien dalam antrian.")

    def tampilkan_antrian(self):
        if self.antrian:
            print("Daftar antrian pasien:")
            for pasien in self.antrian:
                print(pasien)
        else:
            print("Tidak ada pasien dalam antrian.")

def main():
    klinik = Klinik()

    while True:
        print("\n1. Daftar Pasien")
        print("2. Panggil Pasien")
        print("3. Tampilkan Antrian")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama = input("Nama Pasien: ")
            klinik.daftar_pasien(nama)

        elif pilihan == "2":
            klinik.panggil_pasien()

        elif pilihan == "3":
            klinik.tampilkan_antrian()

        elif pilihan == "4":
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
