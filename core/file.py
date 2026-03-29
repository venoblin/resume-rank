import os
import spacy
from PyPDF2 import PdfReader


class File:
    nlp = spacy.load("en_core_web_trf")

    def __init__(self, src: str = "") -> None:
        self.src = src
        self.content = ""
        self.file_extension = os.path.splitext(self.src)[1].lower()

        if not self.src:
            return

        try:
            if self.file_extension == ".txt":
                with open(self.src, "r", encoding="utf-8") as file:
                    self.content = file.read()

            elif self.file_extension == ".pdf":
                reader = PdfReader(self.src)
                pages = []

                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        pages.append(text)

                self.content = " ".join(pages)

            else:
                raise ValueError(f"Unsupported file type: {self.file_extension}")

        except FileNotFoundError:
            print("Error: File not found!")
        except Exception as e:
            print(f"Error reading file: {e}")

    def read_file(self) -> str:
        return self.content

    def extract_keywords(self) -> list[str]:
        if not self.content.strip():
            return []

        doc = self.nlp(self.content)

        keywords = [
            chunk.text.strip().lower()
            for chunk in doc.noun_chunks
            if chunk.text.strip() and not chunk.root.is_stop
        ]

        return list(set(keywords))

    def compare_keywords(self, job_description: str) -> float:
        if not job_description.strip():
            return 0.0

        job_doc = self.nlp(job_description)
        job_keywords = {
            chunk.text.strip().lower()
            for chunk in job_doc.noun_chunks
            if chunk.text.strip() and not chunk.root.is_stop
        }

        resume_keywords = set(self.extract_keywords())

        print(resume_keywords)

        union = job_keywords.union(resume_keywords)
        intersection = job_keywords.intersection(resume_keywords)

        return len(intersection) / len(union) if union else 0.0