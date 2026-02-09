# v1.2.0 09/02/2026
# Author: AppInHand-Dev

import config
import qrcode

# Create the QR code
qr = qrcode.QRCode(
    version=config.qr_version,
    error_correction=config.qr_error_correction,
    box_size=config.qr_box_size,
    border=config.qr_border,
)

# Add data to the QR code
qr.add_data(config.data)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(
  fill_color=config.img_fill_color,
  back_color=config.img_back_color
  )

# Save the QR code image
img.save(config.out_image_file)

print(f"QR code generated and saved as '{config.out_image_file}'")