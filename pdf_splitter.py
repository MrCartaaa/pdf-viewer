import os
from pikepdf import Pdf


def split_pages(filename):
    # the target PDF document to split
    try:
        rtn_files = []
        # load the PDF file
        pdf = Pdf.open(filename)
        # make the new splitted PDF files
        new_pdf_files = [Pdf.new() for i in range(len(pdf.pages))]
        # the current pdf file index
        new_pdf_index = 0
        # iterate over all PDF pages
        for n, page in enumerate(pdf.pages):
            # add the `n` page to the `new_pdf_index` file
            new_pdf_files[n].pages.append(page)
            print(f"[*] Assigning Page {n} to the file {n}")
            # make a unique filename based on original file name plus the index
            name, ext = os.path.splitext(filename)
            output_filename = f"{name}-{n}.pdf"
            # save the PDF file
            new_pdf_files[n].save(output_filename)
            print(f"[+] File: {output_filename} saved.")
            rtn_files.append(output_filename)
    except:
        return False, None

    return True, rtn_files

if __name__ == '__main__':
    filename = "/mnt/c/Users/CarterSteele/Documents/Receipt_20230621_0001.pdf"
    split_pages(filename)
