import fitz  # PyMuPDF

# Function to split a PDF into JPG images
def pdf_to_jpg(pdf_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Iterate through each page in the PDF
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Convert the page to a JPG image
        pix = page.get_pixmap()
        image_filename = f'page_{page_number + 1}.jpg'

        # Save the image to the file
        pix.save(image_filename, 'JPEG')

        # Print the progress
        print(f'Page {page_number + 1} saved as {image_filename}')

    # Close the PDF file
    pdf_document.close()

if __name__ == "__main__":
    pdf_file = "your_pdf_file.pdf"  # Replace with your PDF file's path
    pdf_to_jpg(pdf_file)
