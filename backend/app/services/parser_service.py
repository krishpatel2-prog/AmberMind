from pypdf import PdfReader #this library understands pdf structure

class ParserService: #this class is responsible for pdf -> text

    def extract_pages(self, file_path: str):

        reader = PdfReader(file_path) #loads the pdf

        pages = []

        for index , page in enumerate(reader.pages):

            pages.append(
                {
                    "content": page.extract_text() or "",
                    "page": index + 1,
                    "source":file_path
                }
            )
        return pages