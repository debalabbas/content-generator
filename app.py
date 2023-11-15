import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize the model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Define your prompt template
prompt_template = "The person said: {}, and they also said: {}"

def ask_questions():
    # Ask the user a couple of questions
    answer1 = st.text_input('What can I help you with today, ')
    answer2 = st.text_input('Question 2')

    # Feed the answers to the prompt template
    prompt = prompt_template.format(answer1, answer2)

    return prompt

def generate_response(prompt):
    # Encode the prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate a response
    outputs = model.generate(inputs, max_length=150, num_return_sequences=1)

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

def main():
    prompt = ask_questions()
    if st.button('Generate Response'):
        with st.spinner('Generating...'):
            response = generate_response(prompt)
            st.write(response)

if __name__ == "__main__":
    main()