import streamlit as st
import json
import pickle
from src.bpe_tokenizer import get_stats, merge


# Load the JSON files
file_path_itos = "artifacts/itos.json"
file_path_stoi = "artifacts/stoi.json"
file_path_merges = "artifacts/merges.pkl"

with open(file_path_itos, "r") as file:
    itos = json.load(file)

with open(file_path_stoi, "r") as file:
    stoi = json.load(file)

# To load it back
with open(file_path_merges, "rb") as f:
    merges = pickle.load(f)


# Define encode function
def encode(text):
    tokens = [stoi[c] for c in text]
    while len(tokens) >= 2:
        stats = get_stats(tokens)
        pair = min(stats, key=lambda p: merges.get(p, float("inf")))
        if pair not in merges:
            break  # nothing else can be merged
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens


# Define decode function
def decode(ids):
    text = "".join([itos[str(idx)] for idx in ids])
    return text


# Streamlit app
def main():
    st.title("Devanagari Text Tokenizer and Decoder")

    # Layout with two columns
    col1, col2 = st.columns(2)

    # Column 1: Encoding
    with col1:
        st.header("Encode Text")
        input_text = st.text_area("Enter Devanagari Text:", "")
        if st.button("Encode"):
            if input_text:
                try:
                    encoded_tokens = encode(input_text)
                    st.text_area(
                        "Encoded Tokens:", value=str(encoded_tokens), height=200
                    )
                except Exception as e:
                    st.error(f"Error during encoding: {e}")
            else:
                st.warning("Please enter some text to encode.")

    # Column 2: Decoding
    with col2:
        st.header("Decode Tokens")
        input_tokens = st.text_area("Enter Encoded Tokens (as a Python list):", "")
        if st.button("Decode"):
            if input_tokens:
                try:
                    token_list = eval(input_tokens)  # Convert string to list
                    # st.write(len(token_list))
                    # st.write(itos.get)
                    if isinstance(token_list, list) and all(
                        isinstance(i, int) for i in token_list
                    ):
                        decoded_text = decode(token_list)
                        st.text_area("Decoded Text:", value=decoded_text, height=200)
                    else:
                        st.error("Invalid input! Please enter a list of integers.")
                except Exception as e:
                    st.error(f"Error during decoding: {e}")
            else:
                st.warning("Please enter some tokens to decode.")


if __name__ == "__main__":
    main()
