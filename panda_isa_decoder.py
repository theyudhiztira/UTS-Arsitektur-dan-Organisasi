#!/usr/bin/env python3
def panda_isa_decoder(instruction_hex: str) -> dict:
    if len(instruction_hex) != 3:
        raise ValueError("Instruksi harus berupa string heksadesimal 3-digit")

    try:
        instruction_int = int(instruction_hex, 16)
    except ValueError:
        raise ValueError("Format heksadesimal tidak valid")

    instruction_binary = format(instruction_int, "012b")

    opcode_binary = instruction_binary[:4]
    operand_binary = instruction_binary[4:]

    opcode_mapping = {"0001": "LOAD_MEM", "0100": "ADD_REG"}

    opcode_hex = format(int(opcode_binary, 2), "X")
    operand_hex = format(int(operand_binary, 2), "02X")
    operand_decimal = int(operand_binary, 2)

    opcode_name = opcode_mapping.get(opcode_binary, "UNKNOWN")

    return {
        "instruction_hex": instruction_hex.upper(),
        "instruction_binary": instruction_binary,
        "opcode_binary": opcode_binary,
        "opcode_hex": opcode_hex,
        "opcode_name": opcode_name,
        "operand_binary": operand_binary,
        "operand_hex": operand_hex,
        "operand_decimal": operand_decimal,
    }


def display_instruction_analysis(result: dict) -> None:
    print(f"Instruksi: {result['instruction_hex']}")
    print(f"Biner 12-bit: {result['instruction_binary']}")
    print(
        f"-Opcode: {result['opcode_binary']} = {result['opcode_hex']}h = {result['opcode_name']}"
    )
    print(
        f"-Operand: {result['operand_binary']} = {result['operand_hex']}h = {result['operand_decimal']}d"
    )


def process_instruction(hex_instruction: str) -> None:
    try:
        result = panda_isa_decoder(hex_instruction)
        display_instruction_analysis(result)

        if result["opcode_name"] == "LOAD_MEM":
            print(
                f">>> Operasi: Load data dari alamat memori {result['operand_decimal']}"
            )
        elif result["opcode_name"] == "ADD_REG":
            print(
                f">>> Operasi: Add register dengan alamat/nilai {result['operand_decimal']}"
            )
        else:
            print(">>> Operasi: Instruksi tidak dikenal")

    except ValueError as e:
        print(f"Error: {e}")


def run_test_cases() -> None:
    print("TEST CASE (Dari Soal):")
    print("Decode instruksi 42F dan 19A")
    print("=" * 60)

    test_instructions = ["42F", "19A"]

    for i, instruction in enumerate(test_instructions, 1):
        print(f"\nInstruksi {i}: {instruction}")
        print("-" * 30)
        process_instruction(instruction)


def get_hex_input() -> str:
    while True:
        try:
            hex_input = input("Masukkan instruksi hex (3-digit): ").strip().upper()

            if len(hex_input) != 3:
                print("Error: Instruksi harus tepat 3 digit heksadesimal")
                continue

            try:
                int(hex_input, 16)
                return hex_input
            except ValueError:
                print(
                    "Error: Input harus berupa karakter heksadesimal valid (0-9, A-F)"
                )

        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise


def run_interactive_mode() -> None:
    while True:
        print(f"\n{'=' * 60}")
        print("MODE INTERAKTIF")
        print("=" * 60)

        try:
            hex_instruction = get_hex_input()

            print(f"\nHasil Decode Instruksi {hex_instruction}:")
            print("=" * 40)
            process_instruction(hex_instruction)

            print(f"\n{'=' * 60}")
            try:
                lanjut = input("Ingin decode instruksi lain? (y/n): ").strip().lower()
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


def display_instruction_set() -> None:
    print("\nPANDA ISA INSTRUCTION SET:")
    print("=" * 40)
    print("Opcode | Nama Instruksi | Deskripsi")
    print("-" * 40)
    print("0001   | LOAD_MEM       | Load data dari memori")
    print("0100   | ADD_REG        | Add register operation")
    print("-" * 40)


def main() -> None:
    print("PANDA ISA VIRTUAL MACHINE DECODER")
    print("\nArsitektur dan Organisasi")
    print("Kelompok 6")
    print("=" * 60)
    print("\nEmulator Virtual Machine untuk Panda ISA")
    print("Format Instruksi: 12-bit [4-bit Opcode] [8-bit Operand/Alamat]")
    print("Input: Heksadesimal 3-digit")
    print("-" * 60)

    display_instruction_set()

    print("\nPILIHAN MODE:")
    print("1. Jalankan test case dari soal (42F dan 19A)")
    print("2. Input manual (Mode Interaktif)")

    while True:
        try:
            pilihan = input("\nPilih mode (1/2): ").strip()

            if pilihan == "1":
                run_test_cases()
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
