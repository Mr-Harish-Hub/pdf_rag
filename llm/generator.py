from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from config import LLM_MODEL

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL)
model = AutoModelForSeq2SeqLM.from_pretrained(LLM_MODEL)

def generate_answer(context, question):
    prompt = (
        "Answer the question using ONLY the context below.\n"
        "If the answer is not present, say \"Not found\".\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{question}"
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=150
        )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
