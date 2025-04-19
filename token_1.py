from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

model = GPT2LMHeadModel.from_pretrained('gpt2')
def respond(prompt, maxl=50):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=maxl, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

print('Guestion Prompt Response:', respond('What are the benefits of exercise?'), end='\n')
print('Gommand Prompt Response:', respond("List five benifits of exercise."))