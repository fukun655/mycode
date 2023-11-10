import PyPDF2
from gtts import gTTS
import os

def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def text_to_audio(text, output_file="output.mp3", lang="en"):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)
    print(f"Audio file saved at {output_file}")

if __name__ == "__main__":
    pdf_path = "resume.pdf"
    text = pdf_to_text(pdf_path)

    if text:
        text_to_audio(text)
    else:
        print("Failed to extract text from the PDF.")
