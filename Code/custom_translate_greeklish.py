import json
import re


#this code takes the dataset from messenger and removing all the special characters from JSON also translatesthe greeklish
#content (only messages)

# Mapping dictionary for Greeklish to Greek translation
greeklish_to_greek = {
    'a': 'α',
    'b': 'β',
    'g': 'γ',
    'd': 'δ',
    'e': 'ε',
    'z': 'ζ',
    'h': 'η',
    '8': 'θ',
    'th':'θ',
    'i': 'ι',
    'k': 'κ',
    'l': 'λ',
    'm': 'μ',
    'n': 'ν',
    'x': 'χ',
    'o': 'ο',
    'p': 'π',
    'r': 'ρ',
    's': 'σ',
    't': 'τ',
    'y': 'υ',
    'f': 'φ',
    'c': 'χ',
    'q': 'ψ',
    'w': 'ω',
    'v': 'β',
    'πσ': 'ψ'
}

def remove_invalid_characters(text):
    # Use regex to remove invalid control characters
    cleaned_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return cleaned_text

def translate_greeklish_to_greek(greeklish_text):
    # Convert each Greeklish character to Greek using the mapping dictionary
    translated_text = ''.join([greeklish_to_greek.get(char.lower(), char) for char in greeklish_text])
    return translated_text

# Load the JSON data from file
with open('converted_message_23.json', 'r', encoding='utf-8-sig') as file:
    raw_json_data = file.read()

# Remove invalid control characters from the JSON data
cleaned_json_data = remove_invalid_characters(raw_json_data)

# Parse the cleaned JSON data
json_data = json.loads(cleaned_json_data)

# Iterate through each message in the JSON data
for message in json_data['messages']:
    if 'content' in message:
        content = message['content']
        
        # Check if the message has reactions
        if 'reactions' in message:
            # Remove the reactions
            del message['reactions']

        # Translate the content from Greeklish to Greek
        translated_content = translate_greeklish_to_greek(content)

        # Update the content in the message
        message['content'] = translated_content

# Save the modified JSON data to a new file
with open('translated_json_file_one.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print("Translation completed. The translated JSON data is saved in 'translated_json_file_one.json'.")
