import re


# HASH IDENTIFICATION ENGINE


def is_hex(value):
    return bool(re.fullmatch(r"[0-9a-fA-F]+", value))


def identify_hash(hash_value):

    hash_value = hash_value.strip()

    # bcrypt
    if hash_value.startswith(("$2a$", "$2b$", "$2y$")):
        return [
            ("bcrypt", "HIGH", "3200")
        ]

    # Argon2
    if hash_value.startswith("$argon2"):
        return [
            ("Argon2", "HIGH", "N/A")
        ]

    length = len(hash_value)

    # Validate common raw hashes
    if not is_hex(hash_value):
        return [
            ("Unknown / Not Hex", "LOW", "N/A")
        ]

    # 32 chars
    if length == 32:
        return [
            ("MD5", "MEDIUM", "0"),
            ("NTLM", "LOW", "1000"),
            ("MD4", "LOW", "900"),
            ("RIPEMD-128", "LOW", "6000")
        ]

    # 40 chars
    elif length == 40:
        return [
            ("SHA1", "MEDIUM", "100")
        ]

    # 56 chars
    elif length == 56:
        return [
            ("SHA224", "MEDIUM", "1300")
        ]

    # 64 chars
    elif length == 64:
        return [
            ("SHA256", "MEDIUM", "1400"),
            ("SHA3-256", "LOW", "17400")
        ]

    # 96 chars
    elif length == 96:
        return [
            ("SHA384", "MEDIUM", "10800")
        ]

    # 128 chars
    elif length == 128:
        return [
            ("SHA512", "MEDIUM", "1700")
        ]

    return [
        ("Unknown", "LOW", "N/A")
    ]



# SAVE RESULTS


def save_result(text):

    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")



# SINGLE HASH ANALYSIS


def analyze_single_hash():

    hash_value = input("\nEnter Hash: ").strip()

    results = identify_hash(hash_value)

    print("\n========================================")
    print("HASH ANALYSIS")
    print("========================================")

    for algo, confidence, mode in results:

        print(f"Algorithm     : {algo}")
        print(f"Confidence    : {confidence}")
        print(f"Hashcat Mode  : {mode}")
        print("----------------------------------------")

        save_result(
            f"{hash_value} | {algo} | "
            f"{confidence} | Mode {mode}"
        )

    print("Results saved to results.txt")



# FILE SCAN


def scan_file():

    filename = input(
        "\nEnter filename (example: hashes.txt): "
    )

    try:

        with open(filename, "r", encoding="utf-8") as file:

            print("\n========================================")
            print("FILE SCAN RESULTS")
            print("========================================")

            for line in file:

                hash_value = line.strip()

                if not hash_value:
                    continue

                print(f"\nHash: {hash_value}")

                results = identify_hash(hash_value)

                for algo, confidence, mode in results:

                    print(
                        f" -> {algo} | "
                        f"{confidence} | "
                        f"Mode {mode}"
                    )

                    save_result(
                        f"{hash_value} | "
                        f"{algo} | "
                        f"{confidence} | "
                        f"Mode {mode}"
                    )

        print("\nScan completed.")
        print("Results saved to results.txt")

    except FileNotFoundError:

        print("\nFile not found!")



# VIEW RESULTS


def view_results():

    try:

        with open(
            "results.txt",
            "r",
            encoding="utf-8"
        ) as file:

            print("\n========================================")
            print("SAVED RESULTS")
            print("========================================\n")

            print(file.read())

    except FileNotFoundError:

        print("\nNo results available.")



# MAIN MENU

def main():

    while True:

        print("\n========================================")
        print("MINI HASH IDENTIFIER TOOL")
        print("========================================")
        print("1. Analyze Single Hash")
        print("2. Scan Hash File")
        print("3. View Saved Results")
        print("4. Exit")
        print("========================================")

        choice = input("Choose option: ")

        if choice == "1":

            analyze_single_hash()

        elif choice == "2":

            scan_file()

        elif choice == "3":

            view_results()

        elif choice == "4":

            print("\nGoodbye!")
            break

        else:

            print("\nInvalid option!")




if __name__ == "__main__":
    main()