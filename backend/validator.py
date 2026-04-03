from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_match(requirements, proposal_text):
    results = []
    proposal_lines = proposal_text.split("\n")

    for req in requirements:
        embeddings_req = model.encode(req, convert_to_tensor=True)
        best_score = 0
        for line in proposal_lines:
            embeddings_line = model.encode(line, convert_to_tensor=True)
            score = util.cos_sim(embeddings_req, embeddings_line).item()
            best_score = max(best_score, score)
        results.append({"requirement": req, "confidence": best_score})
    return results


