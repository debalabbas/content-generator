# content-generator
To develop a LLM that mimics Justin Welsh, and produces content by taking input from the user

## Data Collection
I have extracted 9 articles from his website on Personal Growth, Business Planning and Social Media Growth.
After that I have created a training dataset by splitting all of them into chunks of 265 words, with 100 overlapping words, to have a better context while training.

## Model Training

I have used `gpt-2` and trained the model using Masked Language Modelling(Next TOekn Prediction), for 150 epochs.

## Inference
I tried some prompting techniques, and found out that the one that primes the latent space of the model works best, have also added the comparrison in the notebook of the results, following is the final prompt:
```
Main Question: <What is the sub question for that category> ?
Dialog 1: Well, first I need to think about <thinking about the category in general> in general.
Dialog 2: Next, maybe I need to figure out how I define the answer. What criteria am I looking to judge on?
Dialog 3: Based on all this, what can I answer ?
```

## Interface
I have developed a streamlit app, that accepts the main category and then asks for a detailed question within that category. Which is then used to generate the answer