from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage


def get_pedido_content(pdf_path):
    resource_manager = PDFResourceManager(caching=True)
    out_text = StringIO()
    la_params = LAParams()
    text_converter = TextConverter(resource_manager, out_text, laparams=la_params)
    fp = open(pdf_path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, text_converter)

    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = out_text.getvalue()

    fp.close()
    text_converter.close()
    out_text.close()

    return text
