import os
import CRUD

if __name__ == "__main__":
    while (True):
    # sistem_operasi = os.name

    # match sistem_operasi:
    #     case "posix": os.system("clear")
    #     case "nt": os.system("cls")

        os.system("clear")

        print("="*31)
        print("   LATIHAN PROGRAM SEDERHANA   ")
        print(" DATABASE PERPUSTAKAAN DIGITAL ")
        print("="*31+"\n")

        CRUD.init_console()

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        print("="*31+"\n")

        match user_option:
            case "1": print("Opsi read")
            case "2": print("Opsi create")
            case "3": print("Opsi update")
            case "4": print("Opsi detete")
            case _: print("SALAH OPSI")

        print("="*31)

        is_done = input("Apakah sudah selesai [Y/N]? ")
        if is_done == "Y" or is_done == "y":
            break

    print("Program telah berakhir.")