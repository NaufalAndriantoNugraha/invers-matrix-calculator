"""
Inverse Matrix Calculator
"""

import os
import numpy as np
from sys import exit
from time import sleep


def main():
    clear_window()
    print("-----------------------------")
    print("| Inverse Matrix Calculator |")
    print("-----------------------------")

    while True:
        print("----------------------------------")
        print("Pilih salasatu opsi yang tersedia!")
        print("[1] Matriks 2 kali 2")
        print("[2] Matriks 3 kali 3")
        print("[3] Buat Matriks Anda Sendiri")
        print("[4] Keluar dari Program")
        print("----------------------------------")
        print("")

        user_choice = int(input("> Input: "))

        match user_choice:
            case 1:
                two_by_two_matrix()
            case 2:
                three_by_three_matrix()
            case 3:
                user_defined_matrix()
            case 4:
                clear_window()
                while True:
                    print("--------------------------------------")
                    print("| Apakah yakin keluar dari program?  |")
                    print("| [y/Y] Ya, keluar dari program.     |")
                    print("| [n/N] Tidak, tetapi di program.    |")
                    print("--------------------------------------")
                    print("")

                    user_choice = input("> Input: ")

                    if user_choice == "y" or user_choice == "Y":
                        clear_window()
                        exit(0)
                    elif user_choice == "n" or user_choice == "N":
                        clear_window()
                        print("-----------------------------")
                        print("| Inverse Matrix Calculator |")
                        print("-----------------------------")
                        break
                    else:
                        clear_window()
                        print("--------------------------------------")
                        print("| Opsi tidak valid.                  |")
                        print("| Mohon masukkan opsi yang tersedia! |")
                        print("--------------------------------------")
            case _:
                clear_window()
                print("--------------------------------------")
                print("| Opsi tidak valid.                  |")
                print("| Mohon masukkan opsi yang tersedia! |")
                print("--------------------------------------")


def clear_window():
    os.system("cls")


def two_by_two_matrix():
    clear_window()
    print("--------------------")
    print("| Matriks 2 kali 2 |")
    print("--------------------")
    print("")
    
    while True:
        matrix = []
        for row in range(1, (2 + 1)):
            current_row = []

            for column in range(1, (2 + 1)):
                print(f"- Masukkan nilai baris {row} kolom {column}")
                current_element = int(input("> Input: "))
                print("")

                current_row.append(current_element)

            matrix.append(current_row)
    
        matrix_array_numpy = np.array(matrix)

        try:
            inverse_matrix = np.linalg.inv(matrix_array_numpy)
            clear_window()
            print("------------------------------------------------------")
            print("Berikut merupakan nilai matriks yang Anda berikan: ")
            print(f"{matrix}")
            print("")

            print("Berikut merupakan inverse matris dari input Anda:")
            print(f"{inverse_matrix}|")
            print("------------------------------------------------------")
            sleep(6)
            print("")
            print("")

            print("-- Kembali ke menu")
            print("")

            print("-----------------------------")
            print("| Inverse Matrix Calculator |")
            print("-----------------------------")
            break

        except:
            print("-----------------------------")
            print("Matriks tidak memiliki invers")


def three_by_three_matrix():
    clear_window()
    print("--------------------")
    print("| Matriks 3 kali 3 |")
    print("--------------------")
    print("")
    
    while True:
        matrix = []
        for row in range(1, (3 + 1)):
            current_row = []

            for column in range(1, (3 + 1)):
                print(f"- Masukkan nilai baris {row} kolom {column}")
                current_element = int(input("> Input: "))
                print("")

                current_row.append(current_element)

            matrix.append(current_row)
    
        matrix_array_numpy = np.array(matrix)

        try:
            inverse_matrix = np.linalg.inv(matrix_array_numpy)
            clear_window()
            print("------------------------------------------------------")
            print("Berikut merupakan nilai matriks yang Anda berikan: ")
            print(f"{matrix}")
            print("")

            print("Berikut merupakan inverse matris dari input Anda:")
            print(f"{inverse_matrix}|")
            print("------------------------------------------------------")
            sleep(6)
            print("")
            print("")

            print("-- Kembali ke menu")
            print("")

            print("-----------------------------")
            print("| Inverse Matrix Calculator |")
            print("-----------------------------")
            break

        except:
            print("-----------------------------")
            print("Matriks tidak memiliki invers")


def user_defined_matrix():
    clear_window()
    print("---------------------------------")
    print("| Matriks dengan Input Pengguna |")
    print("---------------------------------")

    while True:
        print("")
        print("- Masukkan banyak baris!")
        input_row = int(input("> Input: "))
        print("")

        print("- Masukkan banyak kolom!")
        input_column = int(input("> Input: "))

        matrix = []
        clear_window()
        print("---------------------------------")
        print("| Matriks dengan Input Pengguna |")
        print("---------------------------------")
        print("")

        for row in range(1, (input_row + 1)):
            current_row = []

            for column in range(1, (input_column + 1)):
                print(f"- Masukkan nilai baris {row} kolom {column}")
                current_element = int(input("> Input: "))
                print("")

                current_row.append(current_element)

            matrix.append(current_row)
    
        matrix_array_numpy = np.array(matrix)

        try:
            inverse_matrix = np.linalg.inv(matrix_array_numpy)
            clear_window()
            print("------------------------------------------------------")
            print("Berikut merupakan nilai matriks yang Anda berikan: ")
            print(f"{matrix}")
            print("")

            print("Berikut merupakan inverse matris dari input Anda:")
            print(f"{inverse_matrix}|")
            print("------------------------------------------------------")
            sleep(6)
            print("")
            print("")

            print("-- Kembali ke menu")
            print("")

            print("-----------------------------")
            print("| Inverse Matrix Calculator |")
            print("-----------------------------")
            break

        except:
            print("-----------------------------")
            print("Matriks tidak memiliki invers")


if __name__ == "__main__":
    main()
