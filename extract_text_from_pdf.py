from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def extract_text_from_pdf(pdf_data):
    # Create resource manager
    resource_manager = PDFResourceManager()

    # Create StringIO object to hold extracted text
    extracted_text = StringIO()

    # Create layout analyzer
    layout_analyzer = LAParams()

    # Create text converter object
    text_converter = TextConverter(resource_manager, extracted_text, laparams=layout_analyzer)

    # Create PDF page interpreter object
    page_interpreter = PDFPageInterpreter(resource_manager, text_converter)

    # Initialize dictionary to hold extracted text
    page_dict = {}

    # Open the PDF data in binary mode and extract text from each page
    for page_number, page in enumerate(PDFPage.get_pages(pdf_data, caching=True, check_extractable=True)):
        # Create StringIO object to hold text from current page
        page_text = StringIO()
        page_interpreter.process_page(page)
        page_text.write(extracted_text.getvalue())
        page_text.seek(0)
        # Add the page text to the dictionary with the page number as the key
        page_dict[page_number+1] = page_text.read()
        extracted_text.seek(0)
        extracted_text.truncate()

    # Close the text converter and the StringIO object
    text_converter.close()
    extracted_text.close()

    # Return the dictionary of extracted text
    return page_dict

