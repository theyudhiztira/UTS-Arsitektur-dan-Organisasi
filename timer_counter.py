#!/usr/bin/env python3
class TimerCounter:
    def __init__(self):
        self._value = 0

    @property
    def value(self) -> int:
        return self._value

    def tick(self) -> None:
        self._value = (self._value + 1) % 256

    def reset(self) -> None:
        self._value = 0

    def set_value(self, value: int) -> None:
        if not 0 <= value <= 255:
            raise ValueError("Nilai counter harus antara 0-255")
        self._value = value


def simulate_temperature_logging(start_value: int, end_value: int) -> None:
    counter = TimerCounter()
    counter.set_value(start_value)

    print(f"Mulai monitoring suhu dari counter value: {counter.value}")
    print("-" * 40)

    current = start_value
    cycle_count = 0

    while True:
        print(
            f"Counter: {counter.value:3d} (0x{counter.value:02X}) - Catat suhu sensor"
        )

        if counter.value == end_value:
            print(f"Monitoring selesai pada counter value: {end_value}")
            break

        counter.tick()
        current = (current + 1) % 256

        if current == 0:
            cycle_count += 1
            print(f">>> Counter overflow - Siklus ke-{cycle_count} dimulai")


def run_test_case() -> None:
    print("\nTEST CASE (Dari Soal):")
    print("Tracking waktu dari counter 254 hingga 1")
    print("=" * 50)

    simulate_temperature_logging(254, 1)


def get_user_input() -> tuple[int, int]:
    while True:
        try:
            start = int(input("Masukkan nilai awal counter (0-255): "))
            if not 0 <= start <= 255:
                print("Error: Nilai harus antara 0-255")
                continue
            break
        except ValueError:
            print("Error: Input harus berupa angka")
        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise

    while True:
        try:
            end = int(input("Masukkan nilai akhir counter (0-255): "))
            if not 0 <= end <= 255:
                print("Error: Nilai harus antara 0-255")
                continue
            break
        except ValueError:
            print("Error: Input harus berupa angka")
        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise

    return start, end


def run_interactive_mode() -> None:
    while True:
        print(f"\n{'=' * 50}")
        print("MODE INTERAKTIF")
        print("=" * 50)

        try:
            start_val, end_val = get_user_input()

            print(f"\nSimulasi monitoring dari {start_val} hingga {end_val}:")
            print("=" * 50)

            simulate_temperature_logging(start_val, end_val)

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
    print("8-BIT TIMER COUNTER SIMULATOR")
    print("\nArsitektur dan Organisasi")
    print("Kelompok 6")
    print("=" * 50)
    print("\nReal-time Embedded System Counter")
    print("Simulasi counter biner 8-bit untuk sinkronisasi timer")
    print("Counter range: 0-255 (modulo 256)")
    print("-" * 50)

    print("\nPILIHAN MODE:")
    print("1. Jalankan test case dari soal (254 → 1)")
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
