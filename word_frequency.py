STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def normalize_text(text):
    """Given a text, lowercases it, removes all punctuation, and replaces all whitespace with normal spaces. Multiple whitespace will be compressed into a single space."""
    
    # normalize all words to lowercase
        text = text.casefold()
        valid_chars = string.ascii_letters + string.whitespace +string.digits
        
        # remove punctuation
        new_text = ""
        for char in text:
            if char in valid_chars:
                new_text += char
        
        text = new_text
        text = text.replace("\n", " ")
        return text


def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""

    # Use [open] to read text file [with] auto closes file when done
    with open(filename) as file:
        text = file.read()

    text = normalize_text(text)
    words = []
    # remove "stop words" -- words used so frequently they are ignored
    for word in text.split(" "):
        if word != '' and word not in STOP_WORDS:
            words.append(word)
    

     ## What now?
    # Get a dictionary of word frequencies and print it out
    print(words)

# go through the file word by word and keep a count of how often each word is used


# Calculate the frequency of words in a file




# boiler plate to run in command line 
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
