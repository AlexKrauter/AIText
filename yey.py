from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
def generate(prompt, max_length=100):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, num_return_sequences=1)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story


story = []
story.append(input("Enter the input: "))

def textstory(story):
    result = ''
    for idx, text in enumerate(story):
        result += ("User Input:" if idx == 0 elif "' User Input: '" idx % 2 == 0 else "' Response: " '') + text
    return result
#print(f"Story: {generate(f'Context: the user is in a grassy field, User Input: {input()}',10)}\n")
print(textstory(["a", "what", "b", "THOMG", "cccc5432"]))