import pdfplumber

def extract_requirements(file_path):
    requirements = []
    keywords = ["shall", "must", "required", "mandatory"]

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    if any(word in line.lower() for word in keywords):
                        requirements.append(line.strip())
    return requirements