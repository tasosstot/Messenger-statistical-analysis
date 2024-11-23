# Converting Greeks symbols to UTF-8

import json

# Read the JSON file with unicode-escape encoding
with open("message_1.json", "r", encoding="unicode-escape") as file:
    json_content = file.read()

# Convert the JSON content to UTF-8
converted_json_content = json_content.encode("latin1").decode("utf-8")

# Save the converted JSON to a new file
output_file_path = "converted_message_23.json"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(converted_json_content)

print(f"Converted JSON saved to: {output_file_path}")
