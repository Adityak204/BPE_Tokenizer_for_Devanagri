import os
import re
from tqdm import tqdm


def clean_devanagari_text(text):
    """
    Cleans the given Devanagari text by removing newline characters, extra spaces, and English letters.

    Args:
        text (str): The input text containing Devanagari script.

    Returns:
        str: The cleaned Devanagari text.
    """
    # Remove newline characters
    text = re.sub(r"\n", " ", text)

    # Regex pattern to match anything that is not Devanagari letters, punctuation, or numbers
    pattern = r'[^0-9\u0900-\u097F.,!?;:()\'"—-₹₹\s]'
    text = re.sub(pattern, "", text)

    # Regex pattern to match Devanagari words and separate it from other characters
    pattern = r"([\u0900-\u097F]+)"  # Matches Devanagari characters
    text = re.sub(pattern, r" \1 ", text)  # Add spaces around Devanagari words

    # Add space before danda (।) and double danda (॥)
    pattern = r"([\u0964\u0965])"  # Matches danda and double danda
    text = re.sub(pattern, r" \1 ", text)  # Add spaces around danda and double danda

    # Replace following : \u202c \u202a \u2061
    text = re.sub(r"\u202c", "", text)
    text = re.sub(r"\u202a", "", text)
    text = re.sub(r"\u2061", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def read_txt_files(folder_path="", clean_text=True, data_percentage_limit=1.0):
    """
    Reads all .txt files in the given folder and returns their content as a list.

    Args:
        folder_path (str): The path to the folder containing .txt files.

    Returns:
        list: A list containing the content of each .txt file.
    """
    content_list = []
    num_files_to_read = int(len(os.listdir(folder_path)) * data_percentage_limit)
    num_files_read = 0

    # Iterate through all files in the folder
    for filename in tqdm(os.listdir(folder_path)):
        num_files_read += 1
        if num_files_read > num_files_to_read:
            break
        else:
            # Check if the file has a .txt extension
            if filename.endswith(".txt"):
                file_path = os.path.join(folder_path, filename)

                # Open the file and read its content
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    if clean_text:
                        clean_content = clean_devanagari_text(content)
                    else:
                        clean_content = content
                    content_list.append(clean_content)

    return content_list
