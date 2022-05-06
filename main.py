# Text to Speech Library helps to speak
import pyttsx3

# PDF Toolkit Library to extract PDF Info
import PyPDF2

# Opening the book
book = open('Java.pdf', 'rb')

# Reading Contents
pdfReader = PyPDF2.PdfFileReader(book)

# calculating no of pages in PDF
pages = pdfReader.numPages
print(pages)

# initializing speech engine
speaker = pyttsx3.init()

# Retrieving a page [mention less than no7-1]
page = pdfReader.getPage(29)

# getting text
text = page.extractText()

# Speaker will start reading
speaker.say(text)

# Speech Audio-Enable
speaker.runAndWait()
