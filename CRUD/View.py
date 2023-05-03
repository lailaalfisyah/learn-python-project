from. import Operation

def read_console():
    data_file = Operation.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*102)
    print(f"| {index:4} | {judul:40} | {penulis:40} | {tahun:4} |")
    print("-"*102)

    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")

        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4][:-1]

        print(f"| {index+1:4} | {judul:.40} | {penulis:.40} |  {tahun:4} |")

    # Footer
    print("="*102+"\n")

def create_console():
    print("="*102)
    print("Form Tambah Data Buku\n")

    judul = input("Judul buku: ")
    penulis = input("Penulis buku: ")

    while(True):
        try:
            tahun = int(input("Tahun terbit: "))
            break
        except:
            print("Tahun harus angka. Silakan input kembali. (YYYY)")

    Operation.create(judul, penulis, tahun)
    print("Data buku telah ditambahkan.")
            
def update_console():
    read_console()
    no_buku = int(input("Pilih nomor urut buku yang akan di-update: "))
    data_buku = Operation.read(index=no_buku-1)
    print(data_buku)