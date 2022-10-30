import PyPDF2
import textract
def read_resume(byted_data,ext):
    if ext =='application/pdf':
        with open("temp.pdf", 'wb') as f:
            f.write(byted_data)
        #text1 = textract.process("D:/MSc DATA SCIENCE/sem 5/ML project/temp.pdf")
        #text1 = text1.decode()
        pdfFileObj = open('temp.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        n = pdfReader.numPages
        text = ''
        for i in range(n):
            pageObj = pdfReader.getPage(i)
            text += pageObj.extractText()
        pdfFileObj.close()
        return text
    elif ext == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        with open("temp.docx", 'wb') as f:
            f.write(byted_data)
        text1 = textract.process("D:/MSc DATA SCIENCE/sem 5/ML project/temp.docx")
        text1 = text1.decode()
        return text1


