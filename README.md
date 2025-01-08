# Tokenizer (BPE) for Devanagari script (Hindi)
This repository contains the code for training a Byte Pair Encoding (BPE) tokenizer for Hindi language.
BPE is a subword tokenization algorithm that is used in many NLP tasks. It is a simple algorithm that merges the most frequent pair of characters in a corpus to create a new token. This process is repeated for a fixed number of times or until the vocabulary size reaches a predefined limit.

## Huggingface Space
The tokenizer has been uploaded to the Huggingface space. You can directly interact with tokenizer on this app: [Huggingface Space](https://huggingface.co/spaces/Adityak204/BPE_Tokenizer_for_Devanagri)

## Key Highlights
- Custom BPE tokenizer has been created
- In utf-8 encoding Hindi characters/phoenemes are stored as 3 bytes, in this implementation, we are considering each hindi character as a single byte. (Why should Latin have all the fun?)
- The vocab size is 3000. BPE has managed to compress the original token count by 3.29X
```
Initial number of token: 2349074
Final number of token: 713710
compression ratio: 3.29X
```