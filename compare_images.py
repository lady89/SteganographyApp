from PIL import Image

# Buka kedua gambar
cover_image = Image.open('Static/cover.png')
stego_image = Image.open('Static/stego.png')

# Dapatkan data piksel dari kedua gambar
pixels_cover = cover_image.getdata()
pixels_stego = stego_image.getdata()

# Periksa perbedaan pada piksel
differences = [(a, b) for a, b in zip(pixels_cover, pixels_stego) if a != b]

print(f"Jumlah piksel yang berbeda: {len(differences)}")
