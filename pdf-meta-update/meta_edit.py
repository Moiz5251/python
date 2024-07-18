import pikepdf

def edit_pdf_metadata(input_pdf, output_pdf, metadata):
    with pikepdf.open(input_pdf) as pdf:
        # Delete existing metadata keys
        for key in list(pdf.docinfo.keys()):
            del pdf.docinfo[key]
        # Update with new metadata
        for key, value in metadata.items():
            pdf.docinfo[key] = value
        pdf.save(output_pdf)

# Example usage
input_pdf = 'example.pdf'
output_pdf = 'example_with_metadata.pdf'
metadata = {
    '/Title': 'Download Brochure',
    '/Author': 'Califorca Trading LLC',
    '/Subject': 'Brochure',
    '/Keywords': 'Cleaning Accessories'
}

edit_pdf_metadata(input_pdf, output_pdf, metadata)
