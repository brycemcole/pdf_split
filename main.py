import os
import PyPDF2
import tkinter as tk
from tkinter import filedialog


def split_pdf(input_pdf_path, pages_per_part, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with open(input_pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)

        part_number = 1
        for start in range(0, total_pages, pages_per_part):
            writer = PyPDF2.PdfWriter()
            end = min(start + pages_per_part, total_pages)

            for page in range(start, end):
                writer.add_page(reader.pages[page])

            output_filename = os.path.join(
                output_folder, f'part_{part_number}.pdf')
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)
                print(f'Created: {output_filename}')

            part_number += 1


def main():
    root = tk.Tk()
    root.withdraw()  # we don't want a full GUI, so keep the root window from appearing

    # show an "Open" dialog box and return the path to the selected file
    input_pdf_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")])
    if not input_pdf_path:
        print("No file selected. Exiting.")
        return

    pages_per_part = int(input("Enter the number of pages per part: "))
    output_folder = input("Enter the name of the output folder: ")

    split_pdf(input_pdf_path, pages_per_part, output_folder)


if __name__ == "__main__":
    main()
