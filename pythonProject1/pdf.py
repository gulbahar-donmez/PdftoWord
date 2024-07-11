from pdf2docx import Converter
pdf_path = "C:\\Users\\Gulbahar-NB\\Desktop\\Yeni klasör (2)\\sample2.pdf"
docx_path="C:\\Users\\Gulbahar-NB\\Desktop\\Yeni klasör (2)\\donusturulmus.docx"

cv=Converter(pdf_file=pdf_path)
cv.convert(docx_filename=docx_path)
cv.close()

