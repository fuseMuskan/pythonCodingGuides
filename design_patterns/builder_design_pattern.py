# Product
class Document:
    def __init__(self):
        self.content = ""

    def add_content(self, content):
        self.content += content + "\n"

    def get_content(self):
        return self.content


# Builder interface
class DocumentBuilder:
    def create_document(self):
        self.document = Document()

    def add_title(self, title):
        pass

    def add_heading(self, heading):
        pass

    def add_paragraph(self, paragraph):
        pass

    def get_document(self):
        return self.document


# Concrete Builder for PDF documents
class PDFDocumentBuilder(DocumentBuilder):
    def add_title(self, title):
        self.document.add_content(f"PDF Title: {title}")

    def add_heading(self, heading):
        self.document.add_content(f"PDF Heading: {heading}")

    def add_paragraph(self, paragraph):
        self.document.add_content(f"PDF Paragraph: {paragraph}")



# Director
class DocumentGenerator:
    def __init__(self, builder):
        self.builder = builder

    def generate_document(self, title, headings, paragraphs):
        self.builder.create_document()
        self.builder.add_title(title)
        for heading in headings:
            self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)

    def get_document(self):
        return self.builder.get_document()


if __name__ == "__main__":
    pdf_builder = PDFDocumentBuilder()

    generator = DocumentGenerator(pdf_builder)
    generator.generate_document("My PDF Document", ["Heading 1", "Heading 2"], ["Paragraph 1", "Paragraph 2"])
    pdf_document = generator.get_document()
    print("PDF Document:")
    print(pdf_document.get_content())

