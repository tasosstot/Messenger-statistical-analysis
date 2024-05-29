Facebook analysis with python and pandas

In this project we analyse the basic statistics of Messenger chat history.
Facebook provides the JSON file of all your chats in messenger in which it contains the timestamps of the messages,
the content itself, the author and the reactions. with the help of python and pandas we can collect the statistical data in an Excel file and visualise them in bar charts.

The information we collect is as follows:
    1. The number of messages
    2. The number of words
    3. The most used words
    5. Reactions 

Just download the JSON file of your messenger chat (Click on the link to find out how https://www.bitrecover.com/blog/download-facebook-messenger-chat-history/)


In this repository you will find the Code folder, which contains the project's code in .py and an .ipynb file. You can simply run the .ipynb in Jupiter notebook environment for instant results,
just rename the field of the input file (with open("message_1_gtms.json", "r", encoding="unicode-escape") as file:) with your JSON file. And the second folder containing the results in jpeg and excel type 
