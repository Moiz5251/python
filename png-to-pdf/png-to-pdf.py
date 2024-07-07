from PIL import Image
import os

def convert_images_to_pdf(image_folder, output_pdf_path):
    # Get all PNG files in the image folder
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]
    image_files.sort()  # Ensure the images are in order

    # Create a list to hold the image objects
    image_list = []

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = Image.open(image_path).convert('RGB')
        image_list.append(image)

    # Save the images as a PDF
    if image_list:
        image_list[0].save(output_pdf_path, save_all=True, append_images=image_list[1:])

# Specify the folder containing the PNG images and the output PDF path
image_folder = 'E:/python/pngtopdf/barcodes'
output_pdf_path = 'combined.pdf'

# Convert images to PDF
convert_images_to_pdf(image_folder, output_pdf_path)

print(f"PDF saved successfully at {output_pdf_path}")
