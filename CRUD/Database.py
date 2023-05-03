from . import Operation

DB_NAME = "data.txt"
TEMPLATE = {
    "pk": "XXXXXX",
    "created": "yyyy-mm-dd",
    "judul": 255*" ",
    "penulis": 255*" ",
    "tahun": "yyyy"
}

def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init selesai")
    except:
        print("Database belum tersedia, silakan input data!")
        Operation.create_first_data()
        