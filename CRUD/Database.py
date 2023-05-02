def init_console():
    try:
        with open("data.txt", "r") as file:
            print("Database tersedia, init selesai")
    except:
        print("Database belum tersedia, silakan input data!")
        with open("data.txt", "w", encoding="utf-8") as file:
            judul = input("Judul buku: ")
            penulis = input("Penulis buku: ")
            tahun = input("Tahun terbit: ")
            data = f"{judul},{penulis},{tahun}"
            file.write(data)