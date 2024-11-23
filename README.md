# Message Analysis Tool

A Python tool for analyzing chat data from JSON files, designed to extract meaningful insights such as message counts, reactions, word usage, and more.

---

## Features

- Counts messages and reactions for each sender.
- Tracks the usage of specific words (e.g., "Καλημέρα").
- Calculates the total number of letters sent by each participant.
- Groups messages by date and day of the week.
- Identifies the most common words based on length.
- Outputs results into easy-to-read Excel files.

---

## Requirements

Ensure the following Python libraries are installed:
- `pandas`
- `nltk`
- `openpyxl`

Install them using:
```bash
pip install pandas nltk openpyxl


Workflow 🔄
Step 1: Convert JSON to UTF-8
Run the convertToUTF8.py script to process the raw Facebook JSON file:
Step 2: Translate Greeklish to Greek
python custom_translate_greeklish.py
Step 3: Analyze the Translated Data
python Basic_Stats.py


Outputs 📂
The program generates the following outputs:

Excel Files:

letter_counts.xlsx: Counts the number of letters sent by each user.
message_counts.xlsx: Tracks the total messages sent by each user.
reaction_counts.xlsx: Aggregates reactions for each sender.
word_counts.xlsx: Tracks word usage.
Results_Merged.xlsx: Merged summary of all metrics.
Visualizations:

Saved in the results/diagrams folder, showcasing charts like:
Most active days.
Word frequency distributions.


Limitations ⚠️
Language Support: Currently supports datasets in Greek and Greeklish only.
Facebook-Specific: Designed for Messenger JSON exports.

![alt text](https://dfstudio-d420.kxcdn.com/wordpress/wp-content/uploads/2019/06/digital_camera_photo-1080x675.jpg)
