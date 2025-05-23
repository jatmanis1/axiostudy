from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import io

def compress_pdf(input_pdf, output_pdf, image_quality=50):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        # Check for image streams in the PDF page
        if "/XObject" in page["/Resources"]:
            xobject = page["/Resources"]["/XObject"].get_object()
            for obj in xobject:
                if xobject[obj]["/Subtype"] == "/Image":
                    size = (xobject[obj]["/Width"], xobject[obj]["/Height"])
                    data = xobject[obj].get_data()
                    img = Image.open(io.BytesIO(data))

                    # Compress the image
                    img = img.convert("RGB")  # Ensure RGB mode
                    buffer = io.BytesIO()
                    img.save(buffer, format="JPEG", quality=image_quality)
                    buffer.seek(0)

                    # Replace image data in the PDF
                    xobject[obj]._data = buffer.read()

        # Add the page to the writer
        writer.add_page(page)

    # Write the compressed PDF to the output file
    with open(output_pdf, "wb") as output:
        writer.write(output)

    print(f"Compressed PDF saved as: {output_pdf}")

# Example Usage
input_pdf = "sample.pdf"  # Input PDF path
output_pdf = "compressed_sample.pdf"  # Output PDF path

input_pdf =  'electrochem 1.pdf'
# input_pdf = "chem_1_unit4_part1_&_part3_acid_7_base.pdf"  # Input PDF path

# input_pdf = "sample.pdf"  # Replace with your input file path
output_pdf =f"comp_{input_pdf}"  # Replace with your output file path
compress_pdf(input_pdf, output_pdf, image_quality=10)  # Adjust quality
# compress_pdf(input_pdf, output_pdf)


# Example Usage
 # Replace with your input file path
# output_pdf = "compressed_sample1221.pdf"  # Replace with your output file path
# compress_pdf(input_pdf, output_pdf)
