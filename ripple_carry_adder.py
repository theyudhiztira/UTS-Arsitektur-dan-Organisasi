#!/usr/bin/env python3
def AND(a: int, b: int) -> int:
    return a & b


def OR(a: int, b: int) -> int:
    return a | b


def XOR(a: int, b: int) -> int:
    return a ^ b


def full_adder(A: int, B: int, Cin: int) -> tuple[int, int]:
    sum_bit = XOR(XOR(A, B), Cin)
    carry_out = OR(AND(A, B), AND(XOR(A, B), Cin))

    return sum_bit, carry_out


def ripple_carry_adder_4bit(dataA: str, dataB: str) -> tuple[str, int]:
    if len(dataA) != 4 or len(dataB) != 4:
        raise ValueError("Input harus berupa string biner 4-bit")

    for bit in dataA + dataB:
        if bit not in "01":
            raise ValueError("Input hanya boleh mengandung karakter '0' dan '1'")

    carry = 0
    result_bits = []

    for i in range(3, -1, -1):
        bit_a = int(dataA[i])
        bit_b = int(dataB[i])

        sum_bit, carry_out = full_adder(bit_a, bit_b, carry)

        result_bits.insert(0, str(sum_bit))
        carry = carry_out

    sum_4bit = "".join(result_bits)
    final_carry = carry

    return sum_4bit, final_carry


def display_step_by_step(dataA: str, dataB: str) -> None:
    carry = 0
    result_bits = []

    for i in range(3, -1, -1):
        bit_a = int(dataA[i])
        bit_b = int(dataB[i])

        sum_bit, carry_out = full_adder(bit_a, bit_b, carry)

        result_bits.insert(0, str(sum_bit))
        carry = carry_out

    sum_4bit = "".join(result_bits)

    print("Hasil:")
    print(f"Sum 4-bit: {sum_4bit}")
    print(f"Carry-out: {carry}")

    decimal_a = int(dataA, 2)
    decimal_b = int(dataB, 2)
    decimal_result = int(sum_4bit, 2) + (carry * 16)

    print("\nVerifikasi Desimal:")
    print(f"{dataA} = {decimal_a}")
    print(f"{dataB} = {decimal_b}")
    print(f"Hasil = {decimal_a} + {decimal_b} = {decimal_result}")


def get_binary_input(prompt: str) -> str:
    while True:
        try:
            binary_str = input(prompt).strip()

            if len(binary_str) != 4:
                print("Error: Input harus tepat 4 bit")
                continue

            for bit in binary_str:
                if bit not in "01":
                    print("Error: Input hanya boleh mengandung '0' dan '1'")
                    break
            else:
                return binary_str

        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise


def run_test_case() -> None:
    print("\nTEST CASE (Dari Soal):")
    print("1101₂ (13 desimal) + 0011₂ (3 desimal)")
    print("=" * 50)

    dataA = "1101"
    dataB = "0011"

    display_step_by_step(dataA, dataB)

    sum_result, carry_out = ripple_carry_adder_4bit(dataA, dataB)

    print("\nJAWABAN FINAL:")
    print(f"Sum 4-bit: {sum_result}")
    print(f"Carry-out: {carry_out}")


def run_interactive_mode() -> None:
    while True:
        print(f"\n{'=' * 50}")
        print("MODE INTERAKTIF")
        print("=" * 50)

        try:
            dataA = get_binary_input("Masukkan bilangan biner A (4-bit): ")
            dataB = get_binary_input("Masukkan bilangan biner B (4-bit): ")

            display_step_by_step(dataA, dataB)

            print(f"\n{'=' * 50}")
            try:
                lanjut = input("Ingin mencoba input lain? (y/n): ").strip().lower()
                if lanjut not in ["y", "yes", "ya"]:
                    print("Mode interaktif selesai!")
                    break
            except (EOFError, KeyboardInterrupt):
                print("\nMode interaktif selesai!")
                break

        except (KeyboardInterrupt, EOFError):
            print("\nMode interaktif dihentikan oleh user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break


def main() -> None:
    print("4-BIT RIPPLE CARRY ADDER SIMULATOR")
    print("\nArsitektur dan Organisasi")
    print("Kelompok 6")
    print("=" * 50)
    print("\nSistem penjumlahan biner 4-bit menggunakan Full Adder")
    print("Controller mikrokontroler untuk menghitung total stok barang")
    print("-" * 50)

    print("\nPILIHAN MODE:")
    print("1. Jalankan test case dari soal")
    print("2. Input manual (Mode Interaktif)")

    while True:
        try:
            pilihan = input("\nPilih mode (1/2): ").strip()

            if pilihan == "1":
                run_test_case()
                break
            elif pilihan == "2":
                run_interactive_mode()
                break
            else:
                print("Error: Pilihan harus 1 atau 2")

        except (KeyboardInterrupt, EOFError):
            print("\n\nProgram dihentikan oleh user.")
            break
        except Exception:
            print("Error: Input tidak valid")


if __name__ == "__main__":
    main()
