#Install PyPDF2 (if not already installed)
pip install PyPDF2

import PyPDF2
def merge_pdfs(pdf_list, output_filename):
    merger = PyPDF2.PdfMerger()
    for i in pdf_list:
        merger.append(i)    
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")


pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]  
merge_pdfs(pdf_files, "merged_output.pdf")
