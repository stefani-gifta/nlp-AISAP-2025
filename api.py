from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

app = Flask(__name__)

MODEL_DIR = "flan-t5-ai-simple-bot" 

try:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)
except:
    MODEL_DIR = "google/flan-t5-base"
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_DIR)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_input = data.get('message', '')

    if not user_input:
        return jsonify({"reply": "Sorry, no message received."})

    prompt = f"Explain this AI concept with an analogy: {user_input}"
    
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=256
    )

    output_ids = model.generate(
        **inputs,
        max_new_tokens=128,
        num_beams=5,
        temperature=0.7,
        early_stopping=True
    )

    bot_reply = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    print(f"AI Answer: {bot_reply}\n")
    
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
