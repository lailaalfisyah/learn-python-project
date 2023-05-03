from . import Database
from .Util import random_string
import time
import os

def create_first_data():
    judul = input("Judul buku: ")
    penulis = input("Penulis buku: ")
    tahun = input("Tahun terbit: ")
    
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["created"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["judul"] =  judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["created"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    print(data_str)

    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data gagal ditambahkan.")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r", encoding="utf-8") as file:
            content = file.readlines()
            jumlah_buku = len(content)

            if "index" in kwargs:
                index = kwargs["index"]
                if index < 0 or index > jumlah_buku:
                    return False
                else:
                    return content[index]
            else:
                return content    
    except:
        print("Error saat membaca database.")
        return False

def create(judul:str, penulis:str, tahun:int):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["created"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]},{data["created"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data gagal ditambahkan.")

def update(no_buku, pk, created, judul, penulis, tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["created"] = created
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["tahun"] = tahun

    data_str = f'\n{data["pk"]},{data["created"]},{data["judul"]},{data["penulis"]},{data["tahun"]}'

    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(len(data_str)*(no_buku-1))
            file.write(data_str)
    except:
        print("Data gagal di-update")

def delete(no_buku):
    try:
        with open(Database.DB_NAME, "r") as file:
            counter = 0

            while(True):
                content =  file.readline()

                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as file_temp:
                        file_temp.write(content)

                counter += 1
    except:
        print("Database Error!")

    os.remove(Database.DB_NAME)
    os.rename("data_temp.txt", Database.DB_NAME)