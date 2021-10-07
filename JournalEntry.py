"""
User class created to maintain a list of objects in the main
script.
"""
class Entry:
    """
    Constructor
    """
    def __init__(self, entry_day, entry_date, entry_text):
        self.day = entry_day
        self.date = entry_date
        self.entry_text = entry_text
        