import os
import PyPDF2


class PDFSplitter:
    def __init__(self, input_pdf_path, pages_per_part, output_folder):
        self.input_pdf_path = input_pdf_path
        self.pages_per_part = pages_per_part
        self.output_folder = output_folder

    def split(self):
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        with open(self.input_pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)

            part_number = 1
            for start in range(0, total_pages, self.pages_per_part):
                writer = PyPDF2.PdfWriter()
                end = min(start + self.pages_per_part, total_pages)

                for page in range(start, end):
                    writer.add_page(reader.pages[page])

                output_filename = os.path.join(
                    self.output_folder, f'part_{part_number}.pdf')
                with open(output_filename, 'wb') as output_file:
                    writer.write(output_file)
                    print(f'Created: {output_filename}')

                part_number += 1
