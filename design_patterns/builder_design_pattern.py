class Document:
    """Represents a document with content."""

    def __init__(self):
        self.content = ""

    def add_content(self, content):
        """Add content to the document."""
        self.content += content + "\n"

    def get_content(self):
        """Get the document's content."""
        return self.content


class DocumentBuilder:
    """Builder interface for creating documents."""

    def create_document(self):
        """Create a new document."""
        self.document = Document()

    def add_title(self, title):
        """Add a title to the document."""
        pass

    def add_heading(self, heading):
        """Add a heading to the document."""
        pass

    def add_paragraph(self, paragraph):
        """Add a paragraph to the document."""
        pass

    def get_document(self):
        """Get the generated document."""
        return self.document


class PDFDocumentBuilder(DocumentBuilder):
    """Concrete builder for PDF documents."""

    def add_title(self, title):
        """Add a title to the PDF document."""
        self.document.add_content(f"PDF Title: {title}")

    def add_heading(self, heading):
        """Add a heading to the PDF document."""
        self.document.add_content(f"PDF Heading: {heading}")

    def add_paragraph(self, paragraph):
        """Add a paragraph to the PDF document."""
        self.document.add_content(f"PDF Paragraph: {paragraph}")


class DocumentGenerator:
    """Director for generating documents."""

    def __init__(self, builder):
        self.builder = builder

    def generate_document(self, title, headings, paragraphs):
        """Generate a document using the builder."""
        self.builder.create_document()
        self.builder.add_title(title)
        for heading in headings:
            self.builder.add_heading(heading)
        for paragraph in paragraphs:
            self.builder.add_paragraph(paragraph)

    def get_document(self):
        """Get the generated document."""
        return self.builder.get_document()


def main():
    """Main function to generate and display a PDF document."""
    pdf_builder = PDFDocumentBuilder()

    generator = DocumentGenerator(pdf_builder)
    generator.generate_document("My PDF Document", ["Heading 1", "Heading 2"], ["Paragraph 1", "Paragraph 2"])
    pdf_document = generator.get_document()

    print("PDF Document:")
    print(pdf_document.get_content())


if __name__ == "__main__":
    main()
