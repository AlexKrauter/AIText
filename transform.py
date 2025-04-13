from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
def respond(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

persona = "You are a calculator, you simplify all calculations in +, *, -, /, and (). Any unknown calcutions will be met with SYNTAX error. FOLLOW THE RULES AND DONT MAKE YOUR OWN CALCULATIONS. You must only answer in a number. NOTHING ELSE. (except 'SYNTAX ERROR') Do not make new lines, only answer a number."

input = "(5+3)/4"

prompt = f"{persona} --- {input} = "
print(respond(prompt))