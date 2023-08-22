import pandas as pd
import nltk
import json
import string
import argparse
import datetime

from nltk.corpus import stopwords

nltk.download("stopwords")

def clean_text(text):
    """
    Clean text by removing stopwords, symbols, and converting to lowercase.

    Args:
        text (str): The input text.

    Returns:
        str: The cleaned text.
    """
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Remove stopwords and symbols, and convert to lowercase
    cleaned_words = [
        word.lower()
        for word in words
        if word.lower() not in stopwords.words("english") and word not in string.punctuation
    ]

    # Join the cleaned words back into a string
    cleaned_text = " ".join(cleaned_words)
    return cleaned_text

def process_csv(input_file):
    """
    Read a CSV file, clean its text data, and save it as JSON and CSV files.

    Args:
        input_file (str): The path to the input CSV file.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(input_file)

        # Apply the clean_text function to clean the text data
        df['cleaned_text'] = df['text'].apply(clean_text)

        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        # Define the output filenames
        json_output_file = f"{input_file.split('/')[-1]}_{timestamp}_CLEAN.json"
        csv_output_file = f"{input_file.split('/')[-1]}_{timestamp}_CLEAN.csv"

        # Save the cleaned data as JSON and CSV files
        df.to_json(json_output_file, orient='records', lines=True)
        df.to_csv(csv_output_file, index=False)

        print(f"Cleaned data saved as JSON: {json_output_file}")
        print(f"Cleaned data saved as CSV: {csv_output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Clean CSV text data and save as JSON and CSV files.')

    # Add a positional argument for the CSV file path
    parser.add_argument('file_path', type=str, help='Path to the input CSV file')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the function to process the CSV file
    process_csv(args.file_path)

if __name__ == "__main__":
    main()
