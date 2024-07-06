from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter

def generate_barcode_with_text(code, output_filename):
    try:
        # Replace middle dot zeros with standard zeros
        code = code.replace('·', '0')
        
        # Choose the barcode format (e.g., Code39)
        BARCODE = barcode.get_barcode_class('code39')
        
        # Generate barcode with text disabled
        writer_options = {
            'module_height': 15.0,
            'module_width': 0.2,
            'font_size': 0,  # Disable font rendering to avoid text overlap and middle dot zero issue
            'text_distance': 0,
            'write_text': False  # Disable text rendering on the barcode
        }
        
        barcode_instance = BARCODE(code, writer=ImageWriter())
        barcode_image = barcode_instance.render(writer_options)

        # Create a new image with extra space for the text
        font = ImageFont.truetype("arial.ttf", 12)  # Load a standard font
        text_width, text_height = font.getsize(code)
        barcode_width, barcode_height = barcode_image.size
        total_height = barcode_height + text_height + 10

        new_image = Image.new("RGB", (barcode_width, total_height), "white")
        new_image.paste(barcode_image, (0, 0))
        
        # Draw the text below the barcode
        draw = ImageDraw.Draw(new_image)
        x_position = (barcode_width - text_width) / 2
        y_position = barcode_height + 10
        draw.text((x_position, y_position), code, font=font, fill="black")
        
        # Save the new image
        new_image.save(output_filename)
        print(f'Successfully generated barcode for {code} as {output_filename}')
    except Exception as e:
        print(f'Error generating barcode for {code}: {e}')

def generate_barcodes(codes):
    for code in codes:
        output_filename = f'{code}.png'  # Ensure file extension is included
        generate_barcode_with_text(code, output_filename)

if __name__ == "__main__":
    # List of codes to generate barcodes for
    codes = [
        "7364SU114500",
        "76722XL003XL"
        # Add as many codes as you need
    ]

    generate_barcodes(codes)
