"""
The main script to execute sentiment analysis on journal entry data.
"""
#import Journal Entry class
from JournalEntry import Entry

import SentimentAnalysis

def get_journal_entries_text():
    """
    Open and read from journal entry files
    """
    # TODO: Update this section to open and scan text of all files in directory into objects array
    my_file = open("", "r")

    if my_file.mode == 'r':
        file_lines = my_file.readlines()
        entries_list = []

    my_file.close()
    return entries_list

#Call function to obtain array of JournalEntry objects containing string forms of journal text
ENTRIES_LIST = get_journal_entries_text()

# Run sentiment analysis on all journal entries
for entry in ENTRIES_LIST:
    # Print list of journal entries
    print(entry.entry_day)
    print(entry.entry_date)
    
    sentiment_analysis = SentimentAnalysis.get_sentiment_analysis(entry.entry_text)
    print (sentiment_analysis)
    print ('')   

# TODO: Add output of sentiment analysis to CSV for Excel import


print ('')
print ("Journal Analysis complete.")
print ('')
