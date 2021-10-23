# Import sentiment analysis library
from textblob import TextBlob


def get_sentiment_analysis(journal_entry_string):
    """
    Pass string to sentament analysis function and return double value
    """
    #print(journal_entry_string)
    journal_entry_text_blob = TextBlob(journal_entry_string)
    sentiment = journal_entry_text_blob.sentiment
    # Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857)
    sentiment_polarity = journal_entry_text_blob.sentiment.polarity
    #0.39166666666666666
    return sentiment_polarity
