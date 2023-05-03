import os
import CRUD

if __name__ == "__main__":
    os.system("clear")

    print("="*31)
    print("   LATIHAN PROGRAM SEDERHANA   ")
    print(" DATABASE PERPUSTAKAAN DIGITAL ")
    print("="*31+"\n")

    CRUD.init_console()
    
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
        
        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        user_option = input("Masukan opsi: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            case _: print("SALAH OPSI")

        is_done = input("Apakah sudah selesai menjalankan program [Y/N]? ")
        if is_done == "Y" or is_done == "y":
            break

    print("Program telah berakhir.")