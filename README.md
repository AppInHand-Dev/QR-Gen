# QR-GEN — Simple Lightweight QR Generator

QR-Gen is an open source, easy-to-extend QR code generator written in Python. It provides a compact, well-documented example of using the qrcode library to produce PNG or JPEG images with configurable QR version, error correction level, box size, border, foreground and background colors, and output filename.

---

### ✨ Key features

* Simple configuration through config.py.

* Customizable QR parameters: version, error correction, box size, border.

* Color control for foreground and background.

* Image output compatible with common formats; includes a note about converting to RGB for JPEG.

* Compact and extensible codebase suitable for automation, CI pipelines, or learning.

---

### 🎯 Who this is for

* Developers and hobbyists who need a lightweight QR generator for scripts or static assets.

* Designers and product teams creating QR assets for print or digital use.

* Learners exploring the qrcode library in Python.

---

### 🚀 Quick start

* Clone the repository.

* Edit config.py with your data and desired settings (ensure numeric values are plain integers, not tuples).

* Run the main script with Python.

* The generated image will be saved to the path specified in out_image_file.

---

### Requirements

* Python 3.8 or newer
* Dependencies: qrcode

---

### 📜 License

This project is released as open source.
