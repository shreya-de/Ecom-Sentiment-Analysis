from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import csv

ACCESS_TOKEN = '963093120463257601-qROaDEmTKDXmjYel20N1NhEMHj8Q336'
ACCESS_SECRET = 'wseNFLJcwbIg1EE3FaEM1stg4n26O6YqCEy3yE9ipryp7'
CONSUMER_KEY = 'nRECCPxyYOlGbAZ49b6TrGHs8'
CONSUMER_SECRET = '11tKs1oSnJtlAvXNocX3a1VyOYsEhHhcNbzroPuWkLjsmtyiPW'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
tweets_array = []

max_tweets = 1400
batch = 1

last_id = None

while True:
    print('BATCH NO:', batch)
    if last_id is None:
        result = twitter.search.tweets(q='#amazon', lang='en', result_type='recent', count='100')
    else:
        result = twitter.search.tweets(q='#amazon', lang='en', result_type='recent', count='100', max_id=last_id)

    for r in result['statuses'][:-1]:
        tid = r['id']
        text = r['text']
        likes_count = r['favorite_count']
        retweet_count = r['retweet_count']
        temp = (tid, text, likes_count, retweet_count)
        tweets_array.append(temp)

    last_id = result['statuses'][-1]['id']
    batch += 1

    if len(tweets_array) > max_tweets:
        break

with open('amazon_data.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['tid', 'text', 'likes', 'retweets']
    writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')

    # Write the header
    writer.writeheader()

    # Write the rows
    for t in tweets_array:
        elem = dict(zip(fieldnames, t))
        writer.writerow(elem)
