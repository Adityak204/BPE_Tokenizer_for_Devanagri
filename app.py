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
    st.set_page_config(page_title="Devanagari Tokenizer", layout="wide")
    st.title("Devanagari Text Tokenizer and Decoder")
    st.markdown(
        """<style>
            .stTextArea label {
                font-family: 'Arial', sans-serif;
                font-size: 16px;
                color: #333;
            }
            .stTextArea textarea {
                font-family: 'Courier New', monospace;
                font-size: 14px;
            }
            .stButton button {
                font-family: 'Arial', sans-serif;
                font-size: 16px;
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: #45a049;
            }
        </style>""",
        unsafe_allow_html=True,
    )

    # State to persist outputs
    if "encoded_tokens" not in st.session_state:
        st.session_state["encoded_tokens"] = ""
    if "decoded_text" not in st.session_state:
        st.session_state["decoded_text"] = ""

    # Layout with two columns
    col1, col2 = st.columns(2, gap="large")

    # Column 1: Encoding
    with col1:
        st.header("Encode Text")
        input_text = st.text_area("Enter Devanagari Text:", "")
        if st.button("Encode", key="encode_button"):
            if input_text:
                try:
                    st.session_state["encoded_tokens"] = encode(input_text)
                except Exception as e:
                    st.error(f"Error during encoding: {e}")
            else:
                st.warning("Please enter some text to encode.")
        st.text_area(
            "Encoded Tokens:", value=str(st.session_state["encoded_tokens"]), height=200
        )

    # Column 2: Decoding
    with col2:
        st.header("Decode Tokens")
        input_tokens = st.text_area("Enter Encoded Tokens (as a Python list):", "")
        if st.button("Decode", key="decode_button"):
            if input_tokens:
                try:
                    token_list = eval(input_tokens)  # Convert string to list
                    if isinstance(token_list, list) and all(
                        isinstance(i, int) for i in token_list
                    ):
                        st.session_state["decoded_text"] = decode(token_list)
                    else:
                        st.error("Invalid input! Please enter a list of integers.")
                except Exception as e:
                    st.error(f"Error during decoding: {e}")
            else:
                st.warning("Please enter some tokens to decode.")
        st.text_area(
            "Decoded Text:", value=st.session_state["decoded_text"], height=200
        )


if __name__ == "__main__":
    main()
