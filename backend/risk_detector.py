def detect_risks(proposal_text):
    red_flags = ["subject to change", "limited liability", "additional fees", "pending approval"]
    risks = []
    for line in proposal_text.split("\n"):
        for flag in red_flags:
            if flag in line.lower():
                risks.append({"text": line.strip(), "risk": flag})
    return risks