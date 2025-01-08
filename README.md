# Tokenizer (BPE) for Devanagari script (Hindi)
This repository contains the code for training a Byte Pair Encoding (BPE) tokenizer for Hindi language.
BPE is a subword tokenization algorithm that is used in many NLP tasks. It is a simple algorithm that merges the most frequent pair of characters in a corpus to create a new token. This process is repeated for a fixed number of times or until the vocabulary size reaches a predefined limit.

## Huggingface Space
The tokenizer has been uploaded to the Huggingface space. You can directly interact with tokenizer on this app: [Huggingface Space](https://huggingface.co/spaces/Adityak204/BPE_Tokenizer_for_Devanagri)

## Data Used
The data used for training the tokenizer is the Hindi Wikipedia Articles from [Kaggle](https://www.kaggle.com/datasets/disisbig/hindi-wikipedia-articles-172k). Only 1% data has been used for training the tokenizer.

## Key Highlights
- Custom BPE tokenizer has been created
- In utf-8 encoding Hindi characters/phoenemes are stored as 3 bytes, in this implementation, we are considering each hindi character as a single byte. (Why should Latin have all the fun?)
- The vocab size is 3000. BPE has managed to compress the original token count by 3.73X
```
Initial number of token: 2349074
Final number of token: 630144
compression ratio: 3.73X
```

## How to run the app on local
- Clone the repository
```
git clone https://github.com/Adityak204/BPE_Tokenizer_for_Devanagri.git
```
- Create custom conda environment
```
conda create -n hindi_tokenizer python=3.11
conda activate hindi_tokenizer
```
- Install the required libraries
```
pip install -r requirements.txt
```
- Run the app
```
streamlit run app.py
```
