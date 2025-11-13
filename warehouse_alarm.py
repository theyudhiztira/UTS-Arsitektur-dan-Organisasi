#!/usr/bin/env python3
def AND(a: int, b: int) -> int:
    return a & b


def OR(a: int, b: int) -> int:
    return a | b


def NOT(a: int) -> int:
    return 1 - a


def warehouse_alarm_system(
    pintu_terbuka: int,
    sensor_gerak_aktif: int,
    jendela_terbuka: int,
    kunci_master_aktif: int,
) -> int:
    """
    Implementasi fungsi logika sistem alarm gudang
    Returns: status alarm_berbunyi (True/False)
    """
    kondisi_a = AND(pintu_terbuka, sensor_gerak_aktif)
    master_tidak_aktif = NOT(kunci_master_aktif)
    kondisi_b = AND(jendela_terbuka, master_tidak_aktif)
    alarm_berbunyi = OR(kondisi_a, kondisi_b)

    return alarm_berbunyi


def display_analysis(
    p: int,
    g: int,
    j: int,
    m: int,
    result: int,
    kondisi_a: int,
    kondisi_b: int,
) -> None:
    """Display detailed circuit analysis"""
    print(f"   Input Status:")
    print(f"   Pintu Utama (P): {p} ({'Terbuka' if p else 'Tertutup'})")
    print(f"   Sensor Gerak (G): {g} ({'Aktif' if g else 'Tidak Aktif'})")
    print(f"   Jendela Belakang (J): {j} ({'Terbuka' if j else 'Tertutup'})")
    print(f"   Kunci Master (M): {m} ({'Aktif' if m else 'Tidak Aktif'})")

    print(f"\n🚨 Status Alarm: {'🔴 BERBUNYI' if result else '🟢 TIDAK BERBUNYI'}")

    if result:
        reasons: list[str] = []
        if kondisi_a:
            reasons.append("Pintu terbuka DAN sensor gerak aktif")
        if kondisi_b:
            reasons.append("Jendela terbuka DAN kunci master tidak aktif")
        print(f"   Alasan: {' ATAU '.join(reasons)}")
    else:
        print("   Sistem aman - tidak ada kondisi bahaya yang terpenuhi")


def get_user_input() -> tuple[int, int, int, int]:
    """Get user input for all four parameters"""
    print("\nMasukkan status setiap komponen (0 atau 1):")

    while True:
        try:
            pintu = int(input("Pintu Utama (P) [0=Tertutup, 1=Terbuka]: "))
            if pintu not in [0, 1]:
                print("Error: Input harus 0 atau 1")
                continue
            break
        except ValueError:
            print("Error: Input harus berupa angka 0 atau 1")
        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise

    while True:
        try:
            sensor = int(input("Sensor Gerak (G) [0=Tidak Aktif, 1=Aktif]: "))
            if sensor not in [0, 1]:
                print("Error: Input harus 0 atau 1")
                continue
            break
        except ValueError:
            print("Error: Input harus berupa angka 0 atau 1")
        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise

    while True:
        try:
            jendela = int(input("Jendela Belakang (J) [0=Tertutup, 1=Terbuka]: "))
            if jendela not in [0, 1]:
                print("Error: Input harus 0 atau 1")
                continue
            break
        except ValueError:
            print("Error: Input harus berupa angka 0 atau 1")
        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise

    while True:
        try:
            master = int(input("Kunci Master (M) [0=Tidak Aktif, 1=Aktif]: "))
            if master not in [0, 1]:
                print("Error: Input harus 0 atau 1")
                continue
            break
        except ValueError:
            print("Error: Input harus berupa angka 0 atau 1")
        except (EOFError, KeyboardInterrupt):
            print("\nInput dibatalkan.")
            raise

    return pintu, sensor, jendela, master


def run_predefined_scenarios() -> None:
    """Run all predefined test scenarios"""
    print("\nTEST CASE (Dari Soal):")
    print(
        "Pintu Utama terbuka, Sensor Gerak tidak aktif, Jendela Belakang terbuka, Kunci Master aktif"
    )
    print("=" * 60)

    pintu_terbuka = 1
    sensor_gerak_aktif = 0
    jendela_terbuka = 1
    kunci_master_aktif = 1

    # Hitung menggunakan fungsi
    hasil = warehouse_alarm_system(
        pintu_terbuka, sensor_gerak_aktif, jendela_terbuka, kunci_master_aktif
    )

    # Hitung step by step untuk analisis
    kondisi_a = AND(pintu_terbuka, sensor_gerak_aktif)
    master_inverted = NOT(kunci_master_aktif)
    kondisi_b = AND(jendela_terbuka, master_inverted)

    display_analysis(
        pintu_terbuka,
        sensor_gerak_aktif,
        jendela_terbuka,
        kunci_master_aktif,
        hasil,
        kondisi_a,
        kondisi_b,
    )

    # Demonstrasi kasus lain
    print(f"\n{'=' * 60}")
    print("KASUS LAIN - DEMONSTRASI:")
    print("=" * 60)

    test_cases = [
        (1, 1, 0, 1, "Pintu terbuka + Sensor aktif (Alarm harus berbunyi)"),
        (0, 0, 1, 0, "Jendela terbuka + Master tidak aktif (Alarm harus berbunyi)"),
        (0, 0, 0, 1, "Semua aman (Alarm tidak berbunyi)"),
        (1, 1, 1, 0, "Kedua kondisi terpenuhi (Alarm berbunyi)"),
    ]

    for i, (p, g, j, m, description) in enumerate(test_cases, 1):
        print(f"\nKasus {i}: {description}")
        print("-" * 40)

        result = warehouse_alarm_system(p, g, j, m)
        kondisi_a = AND(p, g)
        master_inv = NOT(m)
        kondisi_b = AND(j, master_inv)

        print(f"Input: P={p}, G={g}, J={j}, M={m}")
        print(f"Kondisi A: {p} AND {g} = {kondisi_a}")
        print(f"Kondisi B: {j} AND (NOT {m}) = {j} AND {master_inv} = {kondisi_b}")
        print(f"Alarm: {kondisi_a} OR {kondisi_b} = {result}")
        print(f"Status: {'🔴 BERBUNYI' if result else '🟢 TIDAK BERBUNYI'}")


def run_interactive_mode() -> None:
    """Run interactive mode with user input"""
    while True:
        print(f"\n{'=' * 60}")
        print("🔧 MODE INTERAKTIF")
        print("=" * 60)

        try:
            pintu, sensor, jendela, master = get_user_input()

            # Hitung hasil
            hasil = warehouse_alarm_system(pintu, sensor, jendela, master)
            kondisi_a = AND(pintu, sensor)
            master_inverted = NOT(master)
            kondisi_b = AND(jendela, master_inverted)

            print(f"\n{'=' * 60}")
            print("HASIL USER INPUT")
            print("=" * 60)

            display_analysis(
                pintu,
                sensor,
                jendela,
                master,
                hasil,
                kondisi_a,
                kondisi_b,
            )

            # Tanya apakah mau lanjut
            print(f"\n{'=' * 60}")
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
    print("WAREHOUSE SECURITY ALARM SYSTEM")
    print("Arsitektur dan Organisasi")
    print("Kelompok 6")
    print("=" * 60)
    print("\nSkenario Sistem Keamanan Gudang:")
    print("Alarm akan berbunyi jika SALAH SATU kondisi berikut terpenuhi:")
    print("a. Pintu Utama (P) terbuka DAN Sensor Gerak (G) aktif")
    print("b. Jendela Belakang (J) terbuka DAN Kunci Master (M) TIDAK aktif")
    print("\nRumus Logika: ALARM = (P AND G) OR (J AND NOT M)")
    print("-" * 60)

    # Menu pilihan
    print("\nPILIHAN MODE:")
    print("1. Jalankan semua skenario otomatis")
    print("2. Input manual (Mode Interaktif)")

    while True:
        try:
            pilihan = input("\nPilih mode (1/2): ").strip()

            if pilihan == "1":
                run_predefined_scenarios()
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
