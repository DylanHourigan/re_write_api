import tensorflow as tf
from transformers import TFAutoModelForSeq2SeqLM, AutoTokenizer

# This loads the pegasus model from google and the tokenizer from it
model_name = "tuner007/pegasus_paraphrase"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = TFAutoModelForSeq2SeqLM.from_pretrained(model_name, from_pt=True)

def paraphrase(text):
    # This tokenizes the text and encodes it
    encoded_text = tokenizer.encode(text, return_tensors="tf", max_length=512, truncation=True)

    # This generates the paraphrased text from the encoded text
    paraphrased_output = model.generate(encoded_text, max_length=512, num_return_sequences=1, temperature=0.7)
    paraphrased_text = tokenizer.decode(paraphrased_output[0], skip_special_tokens=True)

    return paraphrased_text
