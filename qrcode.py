import qrcode


def generate_qr():
    data = input("Enter the text or URL to generate QR Code: ")

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    file_name = input("Enter file name to save QR Code (without extension): ")
    img.save(file_name + ".png")

    print("QR Code generated and saved successfully!")


def main():
    while True:
        print("\n--- QR CODE GENERATOR MENU ---")
        print("1. Generate QR Code")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            generate_qr()
        elif choice == '2':
            print("Exiting QR Code Generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()