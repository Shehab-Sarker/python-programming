import pyttsx3
import PyPDF3
book=open("Theory of Cost.pdf","rb")
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

friend= pyttsx3.init()
for num in range(0,pages):
    pageobj=pdfReader.getPage(0)
    text=pageobj.extractText()
    friend.say(text)
    friend.runAndWait()