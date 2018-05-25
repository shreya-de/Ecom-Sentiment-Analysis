from textblob import TextBlob
import re, csv, json

def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def analyze_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'POSITIVE'
    elif analysis.sentiment.polarity == 0:
        return 'NEUTRAL'
    else:
        return 'NEGATIVE'

def main(path):
    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        rows = []
        for r in reader:
            rows.append(r)

    sentiments = {'POSITIVE':0, 'NEUTRAL':0, 'NEGATIVE':0}
    for row in rows:
        text = row['text']
        polarity = analyze_sentiment(text)
        sentiments[polarity] += 1
    print(json.dumps(sentiments, indent=4))

if __name__ == '__main__':
    path = 'amazon_data.csv'
    main(path)
