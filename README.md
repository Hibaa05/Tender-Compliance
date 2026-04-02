# Tender Compliance Validator

## 📌 Project Overview
The **Tender Compliance Validator** is an automated AI-driven solution designed for Legal and Procurement teams. It eliminates the slow, error-prone manual process of verifying vendor proposals against complex, 100+ page government or corporate tenders (RFPs). 

This system automatically extracts mandatory requirements from an RFP and uses semantic matching to evaluate vendor proposals, immediately flagging any missing or insufficiently addressed clauses.

---

## 🚀 Core Features

### 1. Requirement Extraction Engine
* **Automated Parsing:** Reads RFP documents and generates a structured Master Checklist of mandatory requirements.
* **Keyword Detection:** Identifies mandatory language utilizing keywords such as *"shall," "must," "required,"* and *"mandatory."*
* **Smart Categorization:** Automatically groups requirements into logical categories (e.g., Technical Specifications, Legal Compliance, Financial Terms).
* **Human-in-the-Loop Validation:** Displays extracted requirements in an interactive, editable table so users can verify and confirm before proceeding to the validation phase.

### 2. Bid-to-Requirement Validator
* **Semantic Matching:** Checks the vendor's proposal against the Master Checklist using Natural Language Processing (NLP), understanding context even when the wording differs.
* **Compliance Flagging:** Clearly marks requirements with statuses such as *Met*, *Missing*, or *Insufficiently Addressed*.
* **Confidence Scoring:** Assigns an AI-generated Confidence Score for each match, indicating the system's certainty that the specific requirement was met.

---

## 🛠️ Proposed Tech Stack
*(Note: Update this section based on the final tools used)*
* **Frontend:** Streamlit / React (for the interactive checklist UI)
* **Backend:** Python, FastAPI / Flask
* **NLP / AI Engine:** OpenAI API / HuggingFace Transformers (for semantic matching), spaCy / NLTK (for keyword extraction)
* **Data Handling:** Pandas, PyPDF2 / pdfplumber (for document parsing)

---

## ⚙️ Setup and Installation

Follow these steps to run the application locally.

**1. Clone the repository:**
```bash
git clone [https://github.com/Hibaa05/tender-compliance-validator.git](https://github.com/Hibaa05/tender-compliance-validator.git)
cd tender-compliance-validator
