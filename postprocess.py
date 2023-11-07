import re


def bpe_postprocess(text, bpe_symbol='@@'):
    """
    Post-process the BPE-encoded text to convert it back to normal text.
    :param text: The text output with BPE encoding.
    :param bpe_symbol: The symbol used for BPE merges.
    """
    # Step 2: BPE Decoding
    text = text.replace(bpe_symbol + ' ', '')

    # Step 3: Whitespace Cleanup
    # Remove redundant spaces around punctuation (this step may vary depending on the target language)
    text = re.sub(r'\s+([?.!",](?:\s|$))', r'\1', text)

    return text


# Define your input and output file paths
input_file_path = 'assignments/03/baseline/translations_bpe.txt'
output_file_path = 'assignments/03/baseline/translations_bpe.p.txt'

# Read BPE text, process it, and write the output
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
        open(output_file_path, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        # strip() removes the leading/trailing whitespaces
        decoded_line = bpe_postprocess(line.strip())
        output_file.write(decoded_line + '\n')

print(f"Decoded text has been written to {output_file_path}")


def remove_repetitions(line):
    # Remove immediate word repetitions (words that are next to each other)
    regex_immediate = r'\b(\w+)( \1\b)+'
    line = re.sub(regex_immediate, r'\1', line, flags=re.IGNORECASE)

    # Remove non-immediate word repetitions (words that repeat within a close range)
    words = line.split()
    filtered_words = []
    seen = set()

    # Using a window of words to look for repetitions
    for word in words:
        word_lower = word.lower()
        if word_lower not in seen:
            seen.add(word_lower)
            filtered_words.append(word)
        else:
            # If the word is a repetition and has occurred recently, we skip adding it
            continue

        # Update the 'seen' set to only contain the last N unique words
        if len(seen) > 10:
            seen.remove(filtered_words[-11].lower())

    # Rebuild the line without unnecessary repetitions
    return ' '.join(filtered_words)


# Process the file line by line
cleaned_lines = []
with open('assignments/03/baseline/translations_bpe.p.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # rstrip to remove trailing newlines
        cleaned_line = remove_repetitions(line.rstrip())
        cleaned_lines.append(cleaned_line)

# Combine the cleaned lines with the original line breaks
cleaned_text = '\n'.join(cleaned_lines)

# Write the cleaned text back to a file
with open('assignments/03/baseline/translations_bpe.pp.txt', 'w', encoding='utf-8') as file:
    file.write(cleaned_text)

print("The text with repetitions removed has been saved to 'translations_bpe.pp.txt'.")
