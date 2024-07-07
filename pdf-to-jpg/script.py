from pdf2image import convert_from_path
import os

def pdf_to_jpg(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)
    
    # Save each image as a JPG file
    for i, image in enumerate(images):
        jpg_path = os.path.join(output_folder, f'page_{i + 1}.jpg')
        image.save(jpg_path, 'JPEG')
        print(f'Saved {jpg_path}')

# Example usage
pdf_path = 'E:/python/pdf-to-jpg/damam_brochure.pdf'
output_folder = 'E:/python/pdf-to-jpg/output/'
pdf_to_jpg(pdf_path, output_folder)
