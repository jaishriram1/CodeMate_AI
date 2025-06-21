# model_inference.py

def simulate_model_response(query: str):
    # Replace this with actual model call using Ollama or Hugging Face
    if "invoices for March" in query:
        return [
            {"function": "get_invoices", "args": {"month": "March"}, "assign": "invoices"},
            {"function": "summarize_invoices", "args": {"invoices": "invoices"}, "assign": "summary"},
            {"function": "send_email", "args": {"summary": "summary", "email": "user@example.com"}, "assign": "result"}
        ]
    return []
