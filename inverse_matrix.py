"""
Inverse Matrix Calculator
"""

import os
import platform
from sys import exit
from time import sleep


def main():
    clear_console()
    print("-----------------------------")
    print("| Inverse Matrix Calculator |")
    print("-----------------------------")

    while True:
        print("----------------------------------")
        print("Pilih opsi yang tersedia!")
        print("[1] Buat Matriks Anda Sendiri")
        print("[2] Refresh Console")
        print("[3] Keluar dari Program")
        print("----------------------------------")
        line_break()

        user_choice = int(input("> Input: "))

        match user_choice:
            case 1:
                user_defined_matrix()
            case 2:
                clear_console()
                print("-----------------------------")
                print("| Inverse Matrix Calculator |")
                print("-----------------------------")
            case 3:
                clear_console()
                while True:
                    print("--------------------------------------")
                    print("| Apakah yakin keluar dari program?  |")
                    print("| [y/Y] Ya, keluar dari program.     |")
                    print("| [n/N] Tidak, tetapi di program.    |")
                    print("--------------------------------------")
                    line_break()

                    user_choice = input("> Input: ")

                    if user_choice == "y" or user_choice == "Y":
                        clear_console()
                        exit(0)
                    elif user_choice == "n" or user_choice == "N":
                        clear_console()
                        print("-----------------------------")
                        print("| Inverse Matrix Calculator |")
                        print("-----------------------------")
                        break
                    else:
                        clear_console()
                        print("--------------------------------------")
                        print("| Opsi tidak valid.                  |")
                        print("| Mohon masukkan opsi yang tersedia! |")
                        print("--------------------------------------")
            case _:
                clear_console()
                print("--------------------------------------")
                print("| Opsi tidak valid.                  |")
                print("| Mohon masukkan opsi yang tersedia! |")
                print("--------------------------------------")


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def line_break(size=1):
    print("" * size)


def determinant(matrix):
    matrix_length = len(matrix)

    # Cek banyak elemen matriks
    if matrix_length != len(matrix[0]):
        print("-----------------------------")
        print("| Bukan Matriks Persegi,    |")
        print("| Tidak dapat menghitung    |")
        print("| Determinan                |")
        print("-----------------------------")
        return None

    if matrix_length == 1:
        return matrix[0][0]

    if matrix_length == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(matrix_length):
        # Menentukan tanda positif-negatif kofaktor
        sign = 1 if i % 2 == 0 else -1

        # Menentukan kofaktornya
        cofactor = sign * matrix[0][i] * determinant(minor(matrix, 0, i))
        det += cofactor

    return det


def minor(matrix, row, col):
    minor = []
    for i in range(len(matrix)):
        if i != row:
            minor_row = []

            for j in range(len(matrix[0])):
                if j != col:
                    minor_row.append(matrix[i][j])

            if minor_row:
                minor.append(minor_row)

    return minor


def inverse(matrix):
    det = determinant(matrix)

    if det == 0:
        print("-----------------------------")
        print("| Merupakan Matriks Singular|")
        print("-----------------------------")
        return None

    inv_det = 1 / det
    n = len(matrix)

    result = []
    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        result.append(row)

    for i in range(n):
        for j in range(n):
            sign = 1 if (i + j) % 2 == 0 else -1
            cofactor = sign * determinant(minor(matrix, i, j))
            result[j][i] = cofactor * inv_det

    return result


def print_matrix(matrix, label="Matrix"):
    print(f"{label}:")
    line_break()

    for row in matrix:
        print(row)


def user_defined_matrix():
    clear_console()
    print("---------------------------------")
    print("| Matriks dengan Input Pengguna |")
    print("---------------------------------")
    line_break()

    while True:
        print("- Masukkan ukuran matriks")
        matrix_size = int(input("> Input: "))
        print("")

        matrix = []
        for row in range(matrix_size):
            current_row = []

            for col in range(matrix_size):
                print(f"- Masukkan nilai baris {row + 1} kolom {col + 1}")
                current_element = float(input(f"> Input: "))
                line_break()
                current_row.append(current_element)

            matrix.append(current_row)

        clear_console()

        print_matrix(matrix, "Nilai Matriks yang Anda Berikan")

        inverse_result = inverse(matrix)

        line_break(3)

        if inverse_result:
            print_matrix(inverse_result, "Inverse Matrix dari Input Anda")

        sleep(5)
        line_break()
        print("---------------------")
        print("- Kembali ke Main Menu")
        break


if __name__ == "__main__":
    main()
