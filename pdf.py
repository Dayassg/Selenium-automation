import PyPDF2

with open("dummy.pdf", "rb") as file:
    readers = PyPDF2.PdfReader(file)
    page = readers.pages[0]
    page.rotate(90)

    with open("rotated1.pdf", "wb") as output:
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        writer.write(output)