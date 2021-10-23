"""
The main script to execute sentiment analysis on journal entry data.
"""
#import file list/directory reading libs
from os import listdir
from os.path import isfile, join

#import Journal Entry class
from JournalEntry import Entry

import SentimentAnalysis

journal_directory_path = "C:\\Users\\Patrick\\Desktop\\Journal\\2020\\textFormat"

def get_journal_entry_file_names():
    # get list of files from directory
    journal_entry_file_names = [f for f in listdir(journal_directory_path) if isfile(join(journal_directory_path, f))]
    return journal_entry_file_names

def get_journal_entries_text():
    """
    Open and read from journal entry files
    """
    # TODO: Update this section to open and scan text of all files in directory into objects array
    journal_entry_file_names = get_journal_entry_file_names()

    entries = []
    for entry in journal_entry_file_names:
        #get/set entry day
        entry_day_extension = entry.split(' ')
        entry_day = entry_day_extension[1].split('.')
        
        full_file_path = journal_directory_path + "\\" + entry
        my_file = open(full_file_path, "r")
        
        if my_file.mode == 'r':
            #get/set entry text
            file_lines = my_file.readlines()
            entry_text = ' '.join(file_lines)
            #get/set entry date
            dirty_entry_date = entry_text.splitlines()[1]
            entry_date = dirty_entry_date.strip()
            #get/set entry sentiment
            sentiment_analysis = SentimentAnalysis.get_sentiment_analysis(entry_text)
            #create/append entry
            je = Entry(entry_day[0], entry_date, entry_text,sentiment_analysis)
            entries.append(je)
        my_file.close()
    return entries

#Call function to obtain array of JournalEntry objects containing string forms of journal text
ENTRIES_LIST = get_journal_entries_text()

#Open file we will write tweet ID to
MY_FILE = open("JournalSentiment.txt", "w+")

for entry in ENTRIES_LIST:
    #write entry to CSV
    MY_FILE.write(entry.day +","+ entry.date + "," + str(entry.sentiment) + "\r\n")
    print ("Journal Day: " + entry.day + " captured.")
    print ('')   
# TODO: Add output of sentiment analysis to CSV for Excel import


print ('')
print ("Journal Analysis complete.")
print ('')
