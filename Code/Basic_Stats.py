# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 17:40:20 2023

@author: Tasos
"""

import json
import pandas as pd


# Load the JSON data from file
with open('translated_json_file_one.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)
    
    
    
#   Senders Name Counter 
# Extract the sender_name and count the number of messages for each sender_name
sender_counts = {}
for message in json_data['messages']:
    if 'sender_name' in message:
        sender_name = message['sender_name']
        if sender_name in sender_counts:
            sender_counts[sender_name] += 1
        else:
            sender_counts[sender_name] = 1

# Convert the dictionary to a DataFrame
df = pd.DataFrame(sender_counts.items(), columns=['sender_name', 'message_count'])

# Write the DataFrame to an Excel file
df.to_excel('message_counts.xlsx', index=False)

print("Message counts have been written to 'message_counts.xlsx'.")



#   Senders Reaction Counter 
# Extract the sender_name and count the number of reactions for each sender_name
sender_reaction_counts = {}
for message in json_data['messages']:
    if 'reactions' in message:
        sender_name = message['sender_name']
        reaction_count = len(message['reactions'])
        if sender_name in sender_reaction_counts:
            sender_reaction_counts[sender_name] += reaction_count
        else:
            sender_reaction_counts[sender_name] = reaction_count

# Convert the dictionary to a DataFrame
df = pd.DataFrame(sender_reaction_counts.items(), columns=['sender_name', 'reaction_count'])

# Write the DataFrame to an Excel file
df.to_excel('reaction_counts.xlsx', index=False)

print("Reaction counts have been written to 'reaction_counts.xlsx'.")


#   "Kαλημέρα" Word Counter 
# Define the target words
target_words = ["καλημέρα", "καλημερα"]

# Initialize a dictionary to store the word counts per sender
sender_word_counts = {}

# Iterate through the messages and count the occurrences of the target words for each sender
for message in json_data['messages']:
    if 'sender_name' in message and 'content' in message:
        sender_name = message['sender_name']
        content = message['content']
        content_lower = content.lower()  # Convert to lowercase for case-insensitive matching
        word_count = sum(content_lower.count(word.lower()) for word in target_words)
        if sender_name in sender_word_counts:
            sender_word_counts[sender_name] += word_count
        else:
            sender_word_counts[sender_name] = word_count

# Create a DataFrame from the dictionary
df = pd.DataFrame(sender_word_counts.items(), columns=['Sender Name', 'Word Count'])

# Write the DataFrame to an Excel file
df.to_excel('word_counts.xlsx', index=False)


#   Letters Counter 
# Extract the sender_name and count the number of letters for each sender_name
sender_letter_counts = {}
for message in json_data['messages']:
    if 'sender_name' in message and 'content' in message:
        sender_name = message['sender_name']
        content = message['content']
        letter_count = len(content)
        if sender_name in sender_letter_counts:
            sender_letter_counts[sender_name] += letter_count
        else:
            sender_letter_counts[sender_name] = letter_count

# Convert the dictionary to a DataFrame
df = pd.DataFrame(sender_letter_counts.items(), columns=['sender_name', 'letter_count'])

# Write the DataFrame to an Excel file
df.to_excel('letter_counts.xlsx', index=False)




# List of Excel files to merge
excel_files = ['message_counts.xlsx', 'reaction_counts.xlsx', 'letter_counts.xlsx', 'word_counts.xlsx']

# Read the first Excel file into a DataFrame
merged_df = pd.read_excel(excel_files[0])

# Iterate through the remaining Excel files and merge based on index
for file in excel_files[1:]:
    df = pd.read_excel(file)
    merged_df = merged_df.merge(df, left_index=True, right_index=True)

# Write the merged DataFrame to a new Excel file
merged_df.to_excel('Results.xlsx', index=False)