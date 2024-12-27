import re

def validate_registration(name, phone, email):
    errors = []

    # Validasi nama lengkap
    if not name.isalpha():
        errors.append("Nama lengkap harus hanya berisi huruf.")

    # Validasi nomor telepon
    if not phone.isdigit():
        errors.append("Nomor telepon harus hanya berisi angka.")

    # Validasi email
    email_pattern = r'^\S+@\S+\.\S+$'
    if not re.match(email_pattern, email):
        errors.append("Email harus mengandung karakter '@' dan '.'.")

    # Output hasil validasi
    if errors:
        for error in errors:
            print(error)
    else:
        print("Data pendaftaran valid.")

# Input dari pengguna
name = input("Masukkan nama lengkap: ")
phone = input("Masukkan nomor telepon: ")
email = input("Masukkan email: ")

# Panggil fungsi validasi
validate_registration(name, phone, email)
