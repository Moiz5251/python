import barcode
from barcode.writer import ImageWriter

def generate_barcode(code, output_filename):
    try:
        # Choose the barcode format (e.g., Code39)
        BARCODE = barcode.get_barcode_class('code39')
        # Generate barcode
        barcode_instance = BARCODE(code, writer=ImageWriter())
        # Save the barcode as an image file
        barcode_instance.save(output_filename)
        print(f'Successfully generated barcode for {code} as {output_filename}')
    except Exception as e:
        print(f'Error generating barcode for {code}: {e}')

def generate_barcodes(codes):
    for code in codes:
        output_filename = f'{code}.png'  # Ensure file extension is included
        generate_barcode(code, output_filename)

if __name__ == "__main__":
    # List of codes to generate barcodes for
    codes = [
        "7364SU114500",
         "76722XL003XL"
        # Add as many codes as you need
    ]

    generate_barcodes(codes)
