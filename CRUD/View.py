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

    while(True):
        if data_buku:
            break
        else:
            print("Nomor yang Anda pilih tidak valid.")

    data_break = data_buku.split(",")

    pk = data_break[0]
    created = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        print("\n"+"="*102)
        print("Data yang bisa Anda ubah:")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun}")
        user_option = input("Pilih opsi [1/2/3]: ")
        print("="*102+"\n")

        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3": tahun = int(input("Tahun\t: "))
            case _: print("SALAH OPSI")
    
        print("\n"+"="*102)
        print("Data setelah update:\n")
        print(f"Judul\t: {judul:.40}")
        print(f"Penulis\t: {penulis:.40}")
        print(f"Tahun\t: {tahun}")

        is_done = input("Apakah update sudah sesuai [Y/N]? ")
        if is_done == "Y" or is_done == "y":
            break

    Operation.update(no_buku, pk, created, judul, penulis, tahun)

def delete_console():
    read_console()

    while(True):
        no_buku = int(input("Pilih nomor urut buku yang akan dihapus: "))
        data_buku = Operation.read(index=no_buku-1)

        if data_buku:
            data_break = data_buku.split(",")

            pk = data_break[0]
            created = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            print("\n"+"="*102)
            print("Data yang akan dihapus:\n")
            print(f"Judul\t: {judul:.40}")
            print(f"Penulis\t: {penulis:.40}")
            print(f"Tahun\t: {tahun}")

            is_done = input("Yakin ingin menghapus data [Y/N]? ")
            if is_done == "Y" or is_done == "y":
                Operation.delete(no_buku)
                break
        else:
            print("Nomor yang Anda pilih tidak valid.")
    
    print("Data berhasil dihapus.")