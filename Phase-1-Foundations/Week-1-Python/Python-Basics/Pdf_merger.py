from PyPDF2 import PdfMerger

l=['pdf1.pdf','pdf2.pdf','pdf3.pdf']

mer = PdfMerger()

for m in l:
    mer.append(m)

mer.write('merged1.pdf')

mer.close()