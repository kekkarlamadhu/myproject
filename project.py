import PyPDF2

pdfFileObj = open('Arihant-general_knowledge.pdf', 'rb')  
    
# creating a pdf reader object  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
    
# printing number of pages in pdf file  
print(pdfReader.numPages)  
    
# creating a page object  
#pageObj = pdfReader.getPage(0)  
    
# extracting text from page  
#print(pageObj.extractText())

i=0
while i<pdfReader.numPages:
    pageinfo=pdfReader.getPage(i)
    print(pageinfo.extractText())
    i=i+1
    
# closing the pdf file object  
pdfFileObj.close()  
