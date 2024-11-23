# -*- coding: utf-8 -*-
"""
@author: Tasos
"""

import json
import pandas as pd
import nltk
from collections import Counter

# Download necessary NLTK resources
nltk.download('punkt')

# Load the JSON data from file
with open('translated_json_file_one12.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Initialize dictionaries for metrics
sender_counts = {}
sender_reaction_counts = {}
sender_word_counts = {}
sender_letter_counts = {}
word_counts = {}

# Target words for "Καλημέρα" counter
target_words = ["καλημέρα", "καλημερα"]

# Process messages to calculate metrics
for message in json_data['messages']:
    sender_name = message.get('sender_name')
    if sender_name:
        # Count messages per sender
        sender_counts[sender_name] = sender_counts.get(sender_name, 0) + 1

        # Count reactions per sender
        if 'reactions' in message:
            sender_reaction_counts[sender_name] = sender_reaction_counts.get(sender_name, 0) + len(message['reactions'])

        # Count occurrences of "Καλημέρα" per sender
        content = message.get('content', "")
        content_lower = content.lower()
        kalimera_count = sum(content_lower.count(word) for word in target_words)
        sender_word_counts[sender_name] = sender_word_counts.get(sender_name, 0) + kalimera_count

        # Count letters per sender
        sender_letter_counts[sender_name] = sender_letter_counts.get(sender_name, 0) + len(content)

# Create DataFrames for individual metrics
message_count_df = pd.DataFrame(sender_counts.items(), columns=['sender_name', 'message_count'])
reaction_count_df = pd.DataFrame(sender_reaction_counts.items(), columns=['sender_name', 'reaction_count'])
word_count_df = pd.DataFrame(sender_word_counts.items(), columns=['sender_name', 'word_count_kalimera'])
letter_count_df = pd.DataFrame(sender_letter_counts.items(), columns=['sender_name', 'letter_count'])

# Create a DataFrame from messages and convert timestamp
messages_df = pd.DataFrame(json_data['messages'])
messages_df['datetime'] = pd.to_datetime(messages_df['timestamp_ms'], unit='ms')

# Extract date, time, and day components
messages_df['date'] = messages_df['datetime'].dt.date
messages_df['time'] = messages_df['datetime'].dt.strftime('%H:%M')  # Format time without seconds
messages_df['day'] = messages_df['datetime'].dt.strftime('%A')  # Day of the week

# Group messages by date and aggregate times
message_times = messages_df.groupby('date')['time'].apply(lambda x: ', '.join(x)).reset_index()
message_times_df = pd.DataFrame({'Date': message_times['date'], 'Message Times': message_times['time']})

# Count messages per date
message_counts = messages_df['date'].value_counts().sort_index().reset_index()
message_counts.columns = ['Date', 'Message Count']

# Merge message times and counts into a single DataFrame
result_df = pd.merge(message_times_df, message_counts, on='Date')
result_df = pd.merge(result_df, messages_df[['date', 'day']].drop_duplicates(), left_on='Date', right_on='date')
result_df = result_df[['Date', 'Message Times', 'Message Count', 'day']]

# Group by day of the week and calculate total message count
weekday_summary = result_df.groupby('day')['Message Count'].sum().reset_index()
weekday_summary.columns = ['Day of the Week', 'Total Message Count']

# Save the weekday summary to an Excel file
weekday_summary.to_excel('weekday_summary.xlsx', index=False)
print("Summary of total message counts per day of the week saved to 'weekday_summary.xlsx'.")

# Extract and analyze most-used words (length > 4 and < 10)
messages_df['content'] = messages_df['content'].astype(str)  # Ensure content is string
all_messages = ' '.join(messages_df['content'])
words = nltk.word_tokenize(all_messages)
filtered_words = [word.lower() for word in words if 4 < len(word) < 10]  # Filter words by length
word_counts = Counter(filtered_words)
most_common_words = word_counts.most_common(30)
common_words_df = pd.DataFrame(most_common_words, columns=['Word', 'Frequency'])

# Save individual metrics to Excel files
message_count_df.to_excel('message_counts.xlsx', index=False)
reaction_count_df.to_excel('reaction_counts.xlsx', index=False)
word_count_df.to_excel('word_counts_kalimera.xlsx', index=False)
letter_count_df.to_excel('letter_counts.xlsx', index=False)
common_words_df.to_excel('most_common_words_g4_l10.xlsx', index=False)

print("Individual metric Excel files have been created.")

# Merge all metrics into a single DataFrame
merged_df = message_count_df.merge(reaction_count_df, on='sender_name', how='outer')
merged_df = merged_df.merge(word_count_df, on='sender_name', how='outer')
merged_df = merged_df.merge(letter_count_df, on='sender_name', how='outer')

# Save merged metrics to an Excel file
merged_df.to_excel('Results_Merged.xlsx', index=False)
print("All metrics have been merged and written to 'Results_Merged.xlsx'.")
