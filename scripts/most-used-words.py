import json
import pandas as pd
import nltk
from collections import Counter

# Download the 'punkt' resource
nltk.download('punkt')

# Load the JSON data
with open('translated_json_file_one.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Create a DataFrame from the messages
messages_df = pd.DataFrame(data['messages'])

# Convert the 'content' column to strings, handling any potential NaN values
messages_df['content'] = messages_df['content'].astype(str)

# Combine all message content into a single string
all_messages = ' '.join(messages_df['content'])

# Tokenize the text (split it into words)
words = nltk.word_tokenize(all_messages)

# Convert to lowercase and filter words greater than 4 and less than 10 
words = [word.lower() for word in words if 4 < len(word) < 10 ]

# Count word frequencies
word_counts = Counter(words)

# Get the most common words (e.g., top 10)
most_common_words = word_counts.most_common(30)

# Create a DataFrame for the most common words
common_words_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])

# Convert Frequency column to string
common_words_df['Frequency'] = common_words_df['Frequency'].astype(str)

# Save the most common words to an Excel file
common_words_df.to_excel('most_common_words_over_test_letters.xlsx', index=False)

print("Most common words (over 4 letters) saved to 'most_common_words_over_4_letters.xlsx'.")
