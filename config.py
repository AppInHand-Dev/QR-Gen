# v1.0.0 09/02/2026
# Author: AppInHand-Dev

import qrcode

data = "https://www.example.com/" # Data to be encoded in the QR code
qr_version=1 # QR code version (from 1 to 40)
qr_error_correction=qrcode.constants.ERROR_CORRECT_L # Error correction level
qr_box_size=10 # Size of each QR code box
qr_border=4 # QR code border thickness
img_fill_color="black" # Image box color
img_back_color="white" # Image background color
out_image_file = "qr-image.jpg" # Output file name with extension