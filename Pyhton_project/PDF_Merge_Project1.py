from PyPDF2 import PdfMerger

ALLPDF=["lavcover006.pdf","lavcover07.pdf"]
OurMerger =PdfMerger()

for NewPDF in ALLPDF:
    OurMerger.append(NewPDF)
    
OurMerger.write("Labcover.pdf") 
OurMerger.close()   