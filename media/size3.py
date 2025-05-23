import os
import fitz  # PyMuPDF
from PIL import Image
import io

def compress_pdf(input_pdf, image_quality=50):
    # Generate output file name by appending "_compressed" before the extension
    base_name, ext = os.path.splitext(input_pdf)
    output_pdf = f"{base_name}_compressed{ext}"

    # Open the PDF
    doc = fitz.open(input_pdf)

    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]  # Reference to the image object
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Load image with PIL
            image = Image.open(io.BytesIO(image_bytes))

            # Compress the image
            buffer = io.BytesIO()
            image.save(buffer, format="JPEG", quality=image_quality)
            buffer.seek(0)

            # Replace the image by removing the old one and inserting the compressed version
            compressed_image_bytes = buffer.read()
            rect = fitz.Rect(page.rect)  # Full-page rect as default
            img_rect = fitz.Rect(img[1], img[2], img[3], img[4])  # Position from the image data

            # Draw the compressed image on the same location
            page.insert_image(img_rect, stream=compressed_image_bytes)

    # Save the compressed PDF with the new name
    doc.save(output_pdf)
    doc.close()
    print(f"Compressed PDF saved as: {output_pdf}")

# Example Usage
# input_pdf = "MLF Formula List (_100).pdf"  # Input PDF path
# compress_pdf(input_pdf, image_quality=10)  # Adjust quality as needed

# Example Usage
input_pdf = "chem_1_unit2_part1_S_block.pdf"  # Input PDF path
compress_pdf(input_pdf, image_quality=10)  # Adjust quality as needed
