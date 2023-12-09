import tkinter as tk
from tkinter import filedialog
from pdf_split import PDFSplitter


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    input_pdf_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")])
    if not input_pdf_path:
        print("No file selected. Exiting.")
        return

    pages_per_part = int(input("Enter the number of pages per part: "))
    output_folder = input("Enter the name of the output folder: ")

    splitter = PDFSplitter(input_pdf_path, pages_per_part, output_folder)
    splitter.split()


if __name__ == "__main__":
    main()
