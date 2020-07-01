import PyPDF2
# pdf file object
# To find the pdf file with complete code in below
pdf_File = open('Arihant-general_knowledge.pdf', 'rb')  
    
# creating a pdf reader object  
read_pdf = PyPDF2.PdfFileReader(pdf_File)  
    
# printing number of pages in pdf file  
print(read_pdf.numPages)  
    
# creating a page object  
#pageObj = read_pdf.getPage(0)  
    
# extracting text from page.
# this will print the text you can also save that into String
#print(pageObj.extractText())


#extract entire pdf
#that is  questions, multi choice options and answers from the attached book
i=0
while i<read_pdf.numPages:
    pageinfo=read_pdf.getPage(i)
    print(pageinfo.extractText())
    i=i+1
    
# closing the pdf file object  
pdfFileObj.close()  
