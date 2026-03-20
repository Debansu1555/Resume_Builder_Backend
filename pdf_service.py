from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import io

def generate_pdf(content, password):
    buffer = io.BytesIO()

    c = canvas.Canvas(buffer)
    text = c.beginText(40, 800)

    for line in content.split("\n"):
        text.textLine(line)

    c.drawText(text)
    c.save()

    buffer.seek(0)

    reader = PdfReader(buffer)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    output = io.BytesIO()
    writer.write(output)

    return output.getvalue()