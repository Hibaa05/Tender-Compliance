import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pdfplumber
from backend.extractor import extract_requirements
from backend.validator import semantic_match
from backend.risk_detector import detect_risks

st.title("Tender Compliance Validator")

# Upload RFP
rfp_file = st.file_uploader("Upload RFP Document", type="pdf")
if rfp_file:
    requirements = extract_requirements(rfp_file)
    st.write("### Extracted Requirements")
    for r in requirements:
        st.write("- ", r)

    # Upload Vendor Proposal
    proposal_file = st.file_uploader("Upload Vendor Proposal", type="txt")
    if proposal_file:
        proposal_text = proposal_file.read().decode("utf-8")
        matches = semantic_match(requirements, proposal_text)
        risks = detect_risks(proposal_text)

        st.write("### Validation Results")
        for m in matches:
            st.write(f"{m['requirement']} → Confidence: {m['confidence']:.2f}")

        st.write("### Detected Risks")
        for r in risks:
            st.write(f"⚠️ {r['text']} (Risk: {r['risk']})")