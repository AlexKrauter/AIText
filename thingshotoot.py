from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
def classify(prompt, maxl=50):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=maxl, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.strip()
fewshotprompt = ("Review: 'I love this product' -> Sentiment: Positive\n" +
"Review: 'The item was terrible' -> Sentiment: Negative\n" +
"Review: 'This is an amazing service' -> Sentiment: "
)

print(classify(fewshotprompt))