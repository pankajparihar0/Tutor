import PyPDF2

import re
import os

def split_pdf_chapters(pdf_path, output_dir):
    """
    Splits a PDF into chapters based on its table of contents.

    Args:
        pdf_path: Path to the input PDF file.
        output_dir: Path to the directory where chapter PDFs will be saved.
    """

    try:
        text = pdfminer.high_level.extract_text(pdf_path)
        print("hiii")
        print(text)
        # Improved regex to capture more TOC variations. Adjust as needed.
    #     chapter_info = re.findall(r"(Chapter|PART)\s*(\d+|[IVXLCDM]+)\s*[:\-\.]?\s*(.?)\s(\d+)", text, re.IGNORECASE)

    #     if not chapter_info:
    #         print("Error: Could not find chapter information in the PDF.")
    #         return

    #     chapter_pages = []
    #     for chapter in chapter_info:
    #         try:
    #             chapter_pages.append(int(chapter[3])) # page numbers are in the fourth capture group.
    #         except ValueError:
    #             print(f"Warning: Could not convert page number '{chapter[3]}' to integer. Skipping chapter '{chapter[2]}'.")
    #             continue

    #     if not os.path.exists(output_dir):
    #         os.makedirs(output_dir)

    #     with open(pdf_path, 'rb') as pdf_file:
    #         pdf_reader = PyPDF2.PdfReader(pdf_file)
    #         for i in range(len(chapter_pages)):
    #             start_page = chapter_pages[i]
    #             end_page = chapter_pages[i + 1] - 1 if i + 1 < len(chapter_pages) else len(pdf_reader.pages)

    #             pdf_writer = PyPDF2.PdfWriter()
    #             for page_num in range(start_page - 1, end_page):
    #                 try:
    #                     pdf_writer.add_page(pdf_reader.pages[page_num])
    #                 except IndexError:
    #                     print(f"Warning: Page {page_num+1} out of range in PDF. Skipping.")
    #                     continue

    #             output_filename = os.path.join(output_dir, f"Chapter_{i + 1}.pdf")
    #             with open(output_filename, 'wb') as output_pdf:
    #                 pdf_writer.write(output_pdf)

    #     print(f"Successfully split PDF into chapters. Saved to: {output_dir}")

    # except FileNotFoundError:
    #     print(f"Error: PDF file not found at '{pdf_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
pdf_file_path = "./Data/Raw/iesc101.pdf" # Replace with your PDF file path.
output_directory = "./Data/Processed" # Replace with desired output directory.
split_pdf_chapters(pdf_file_path, output_directory)