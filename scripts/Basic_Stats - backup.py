# -*- coding: utf-8 -*-
"""
@author: Tasos
"""

import json
import pandas as pd

# Load the JSON data from file
with open('translated_json_file_one12.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Initialize dictionaries for counting
sender_counts = {}
sender_reaction_counts = {}
sender_word_counts = {}
sender_letter_counts = {}

# Define the target words for "Καλημέρα" counter
target_words = ["καλημέρα", "καλημερα"]

# Process the messages
for message in json_data['messages']:
    if 'sender_name' in message:
        sender_name = message['sender_name']

        # Count messages per sender
        sender_counts[sender_name] = sender_counts.get(sender_name, 0) + 1

        # Count reactions per sender
        if 'reactions' in message:
            sender_reaction_counts[sender_name] = sender_reaction_counts.get(sender_name, 0) + len(message['reactions'])

        # Count occurrences of "Καλημέρα" per sender
        if 'content' in message:
            content = message['content']
            content_lower = content.lower()  # Case-insensitive matching
            word_count = sum(content_lower.count(word.lower()) for word in target_words)
            sender_word_counts[sender_name] = sender_word_counts.get(sender_name, 0) + word_count

            # Count letters per sender
            sender_letter_counts[sender_name] = sender_letter_counts.get(sender_name, 0) + len(content)

# Create DataFrames for each metric
message_count_df = pd.DataFrame(sender_counts.items(), columns=['sender_name', 'message_count'])
reaction_count_df = pd.DataFrame(sender_reaction_counts.items(), columns=['sender_name', 'reaction_count'])
word_count_df = pd.DataFrame(sender_word_counts.items(), columns=['sender_name', 'word_count'])
letter_count_df = pd.DataFrame(sender_letter_counts.items(), columns=['sender_name', 'letter_count'])

# Save each metric to an individual Excel file
message_count_df.to_excel('message_counts.xlsx', index=False)
reaction_count_df.to_excel('reaction_counts.xlsx', index=False)
word_count_df.to_excel('word_counts_kalimera.xlsx', index=False)
letter_count_df.to_excel('letter_counts.xlsx', index=False)

print("Individual metric Excel files have been created.")

# Merge all metrics into a single Excel file
# Merge DataFrames sequentially
merged_df = message_count_df.merge(reaction_count_df, on='sender_name', how='outer')
merged_df = merged_df.merge(word_count_df, on='sender_name', how='outer')
merged_df = merged_df.merge(letter_count_df, on='sender_name', how='outer')

# Save the merged DataFrame to an Excel file
merged_df.to_excel('Results_Merged.xlsx', index=False)

print("All metrics have been merged and written to 'Results.xlsx'.")
