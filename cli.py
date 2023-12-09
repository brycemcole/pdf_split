import argparse
from pdf_split import PDFSplitter


def main():
    parser = argparse.ArgumentParser(description='Split a PDF into parts.')
    parser.add_argument('-f', '--file', type=str, required=True,
                        help='The path to the PDF file to be split')
    parser.add_argument('-p', '--pages', type=int,
                        required=True, help='Number of pages per part')
    parser.add_argument('-o', '--output', type=str, required=True,
                        help='The output folder for the split PDFs')

    args = parser.parse_args()

    splitter = PDFSplitter(args.file, args.pages, args.output)
    splitter.split()


if __name__ == "__main__":
    main()
