from fastapi import FastAPI, UploadFile
from backend.extractor import extract_requirements
from backend.validator import semantic_match
from backend.risk_detector import detect_risks

app = FastAPI()

@app.post("/extract/")
async def extract(file: UploadFile):
    requirements = extract_requirements(file.file)
    return {"requirements": requirements}

@app.post("/validate/")
async def validate(file: UploadFile, requirements: list):
    text = file.file.read().decode("utf-8")
    matches = semantic_match(requirements, text)
    risks = detect_risks(text)
    return {"matches": matches, "risks": risks}