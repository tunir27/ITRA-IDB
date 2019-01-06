from PyPDF2 import PdfFileReader,PdfFileMerger
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import cm,mm
from reportlab.lib.enums import TA_JUSTIFY


def pdf_creator(my_text):
    def addPageNumber(canvas, doc):
        """
        Add the page number
        """
        page_num = canvas.getPageNumber()
        text = "%s" % page_num
        canvas.drawRightString(200*mm, 20*mm, text)
    def addPageNumber1(canvas, doc):
        """
        Add the page number
        """
        temp_pdf=PdfFileReader(open("output.pdf", "rb"))
        page_num = temp_pdf.getNumPages()+1
        text = "%s" % page_num
        canvas.drawRightString(200*mm, 20*mm, text)


    flag=0
    try:
        existing_pdf = PdfFileReader(open("output.pdf", "rb"))
    except:
        flag=1

    if flag==0:
        elements=[]
        doc = SimpleDocTemplate("test.pdf",pagesize=A4,
                        rightMargin=2*cm,leftMargin=2*cm,
                        topMargin=2*cm,bottomMargin=2*cm)

        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        elements.append(Paragraph(my_text.replace("\n", "<br />"),styles["Justify"]))
        doc.build(elements,onFirstPage=addPageNumber1, onLaterPages=addPageNumber1)

        # Read your existing PDF
        new_pdf=PdfFileReader(open("test.pdf", "rb"))
        #output = PdfFileWriter()
        merger = PdfFileMerger()
        merger.append(existing_pdf)
        merger.append(new_pdf)
        merger.write("output.pdf")
    else:
        elements=[]
        doc = SimpleDocTemplate("output.pdf",pagesize=A4,
                        rightMargin=2*cm,leftMargin=2*cm,
                        topMargin=2*cm,bottomMargin=2*cm)

        styles=getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
        elements.append(Paragraph(my_text.replace("\n", "<br />"),styles["Justify"]))
        doc.build(elements,onFirstPage=addPageNumber, onLaterPages=addPageNumber)



