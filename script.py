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
        print("[3] Keluar dari aplikasi")
        print("----------------------------------")
        print("")

        user_choice = int(input("> Input: "))

        match user_choice:
            case 1:
                two_by_two_matrix()
            case 2:
                three_by_three_matrix()
            case 3:
                clear_window()
                while True:
                    print("--------------------------------------")
                    print("| Apakah yakin keluar dari aplikasi? |")
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

    first_row = []
    second_row = []

    while True:
        for row in range(1, 3):
            for column in range(1, 3):
                if row == 1:
                    # print("--------------------------------------------")
                    print(f"- Masukkan nilai baris {row} kolom {column}")
                    first_row.append(int(input("> Input: ")))
                    print("")
                else:
                    # print("--------------------------------------------")
                    print(f"- Masukkan nilai baris {row} kolom {column}")
                    second_row.append(int(input("> Input: ")))
                    print("")

        matrix_value = np.array(
            [
                first_row,
                second_row
            ]
        )

        clear_window()

        print("---------------------------------------------------")
        print("Berikut merupakan nilai matriks yang Anda berikan: ")
        print(first_row)
        print(second_row)
        print("")

        print("Berikut merupakan inverse matrik dari input Anda:  ")

        try:
            print(np.linalg.inv(matrix_value))
            print("---------------------------------------------------")
        except np.linalg.LinAlgError:
            print("Matriks tidak dapat di invers")

        sleep(6)
        print("")
        print("")

        print("-- Kembali ke menu")
        print("")

        print("-----------------------------")
        print("| Inverse Matrix Calculator |")
        print("-----------------------------")
        break


def three_by_three_matrix():
    clear_window()
    print("--------------------")
    print("| Matriks 3 kali 3 |")
    print("--------------------")

    first_row = []
    second_row = []
    third_row = []

    while True:
        for row in range(1, 4):
            for column in range(1, 4):
                if row == 1:
                    # print("--------------------------------------------")
                    print(f"- Masukkan nilai baris {row} kolom {column}")
                    first_row.append(int(input("> Input: ")))
                    print("")
                elif row == 2:
                    # print("--------------------------------------------")
                    print(f"- Masukkan nilai baris {row} kolom {column}")
                    second_row.append(int(input("> Input: ")))
                    print("")
                else:
                    # print("--------------------------------------------")
                    print(f"- Masukkan nilai baris {row} kolom {column}")
                    third_row.append(int(input("> Input: ")))
                    print("")

        matrix_value = np.array(
            [
                first_row,
                second_row,
                third_row
            ]
        )

        clear_window()

        print("---------------------------------------------------")
        print("Berikut merupakan nilai matriks yang Anda berikan: ")
        print(first_row)
        print(second_row)
        print(third_row)
        print("")

        print("Berikut merupakan inverse matrik dari input Anda:  ")

        try:
            print(np.linalg.inv(matrix_value))
            print("---------------------------------------------------")
        except np.linalg.LinAlgError:
            print("Matriks tidak dapat di invers")

        sleep(6)
        print("")
        print("")

        print("-- Kembali ke menu")
        print("")

        print("-----------------------------")
        print("| Inverse Matrix Calculator |")
        print("-----------------------------")
        break


if __name__ == "__main__":
    main()
