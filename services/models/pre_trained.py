import random
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")  
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws").to('cpu')

def paraphrase(text):
    
    encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to("cpu"), encoding["attention_mask"].to("cpu")
    
    paraphrased_output = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=5
        )
    paraphrases = [tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True) for output in paraphrased_output]
        
    return random.choice(paraphrases)

def paraphrase_all(text):
    encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to("cpu"), encoding["attention_mask"].to("cpu")
    
    paraphrased_output = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        max_length=256,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=15
        )
    paraphrases = set() 
    for output in paraphrased_output:
        paraphrase = tokenizer.decode(output, skip_special_tokens=True, clean_up_tokenization_spaces=True)
        if paraphrase != text:
            paraphrases.add(paraphrase)

    return list(paraphrases)[:5]