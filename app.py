import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("debal/gpt2-finetuned-justin-welsh")
model = GPT2LMHeadModel.from_pretrained("debal/gpt2-finetuned-justin-welsh")

# Define your prompt template
prompt_template = """Main Question: {} ?
Dialog 1: Well, first I need to think about {} in general.
Dialog 2: Next, maybe I need to figure out how I define the answer. What criteria am I looking to judge on?
Dialog 3: Based on all this, what can I answer ?
Answer:"""

def ask_questions():
    # Ask the user a couple of questions
    category = st.radio(
        "Select a category",
        ("Personal Growth", "Business Planning", "Social Media Growth")
    )
    answer = st.text_input(f'What can I help you in {category}')
    print(bool(answer))

    # Feed the answers to the prompt template
    prompt = prompt_template.format(answer,category)
    print(prompt)
    return prompt,answer

def generate_response(prompt):
    # Encode the prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate a response
    outputs = model.generate(
        inputs, 
        max_length=300, 
        num_return_sequences=1, 
        num_beams=3, 
        no_repeat_ngram_size=3, 
        top_k=30, 
        top_p=1)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

def main():
    st.title('Justin Welsh Bot')
    prompt,sub_question = ask_questions()
    if bool(sub_question):
        with st.spinner('Generating...'):
            response = generate_response(prompt)
            # response = response.replace(prompt,"")
            st.write(response[len(prompt)-1:])

if __name__ == "__main__":
    main()