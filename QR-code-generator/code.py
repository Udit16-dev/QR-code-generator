import qrcode
from PIL import Image
import re
import os

# Function to create a safe filename from the URL
def create_filename_from_url(url):
    # Remove protocol and special characters to make a valid filename
    filename = re.sub(r'\W+', '_', url)
    return f"{filename[:50]}.png"  # limit to 50 characters for filename

# Function to generate and display QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    img.show()

    print(f"QR Code has been generated, saved as '{filename}', and displayed.")

# Prompt user to enter image URL
image_url = input("Enter the URL of the image to encode (e.g., https://example.com/landscape.jpg): ")

# Basic URL validation
if image_url.lower().startswith('http'):
    filename = create_filename_from_url(image_url)
    generate_qr_code(image_url, filename)
else:
    print("Invalid URL. Please make sure it starts with 'http'.")
