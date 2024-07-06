from barcode import generate
from barcode.writer import ImageWriter
from PIL import Image

# Define the barcode data
data = "B09L5DF5NQR"  # Replace this with your custom barcode data

# Generate the barcode using a custom format (e.g., code128)
barcode = generate('code128', data, writer=ImageWriter())

# Save the barcode as an image (PNG format)
png_filename = barcode.save('custom_barcode')

# Open the PNG image
img = Image.open(png_filename)

# Convert and save the image as JPG
jpg_filename = 'custom_barcode.jpg'
img.convert('RGB').save(jpg_filename, 'JPEG')

print(f"Barcode saved as {jpg_filename}")
