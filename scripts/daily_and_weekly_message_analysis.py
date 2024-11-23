import json
import pandas as pd

# Load the JSON data
with open('translated_json_file_one.json', 'r', encoding='utf-8-sig') as file:
    data = json.load(file)

# Create a DataFrame from the messages
messages_df = pd.DataFrame(data['messages'])

# Convert timestamp_ms to datetime
messages_df['datetime'] = pd.to_datetime(messages_df['timestamp_ms'], unit='ms')

# Extract the date, time, and day components
messages_df['date'] = messages_df['datetime'].dt.date
messages_df['time'] = messages_df['datetime'].dt.strftime('%H:%M')  # Format time without seconds
messages_df['day'] = messages_df['datetime'].dt.strftime('%A')  # Get the day of the week

# Group messages by date and aggregate the times into a single cell
message_times = messages_df.groupby('date')['time'].apply(lambda x: ', '.join(x)).reset_index()

# Create a DataFrame to store the message times
message_times_df = pd.DataFrame({'Date': message_times['date'], 'Message Times': message_times['time']})

# Count the number of messages for each day
message_counts = messages_df['date'].value_counts().sort_index().reset_index()
message_counts.columns = ['Date', 'Message Count']

# Merge the message times and message counts DataFrames
result_df = pd.merge(message_times_df, message_counts, on='Date')

# Merge the day column with the result DataFrame
result_df = pd.merge(result_df, messages_df[['date', 'day']].drop_duplicates(), left_on='Date', right_on='date')

# Remove the first column
result_df = result_df[['Date', 'Message Times', 'Message Count', 'day']]

# Save the result to an XLSX file
result_df.to_excel('222.xlsx', index=False)

print("Message times, counts, and days per day saved to '222.xlsx'.")

# Group by the day of the week and sum the message counts
weekday_summary = result_df.groupby('day')['Message Count'].sum().reset_index()

# Rename columns for clarity
weekday_summary.columns = ['Day of the Week', 'Total Message Count']

# Save the weekday summary to a new Excel file
weekday_summary.to_excel('weekday_summary.xlsx', index=False)

print("Summary of total message counts per day of the week saved to 'weekday_summary.xlsx'.")
