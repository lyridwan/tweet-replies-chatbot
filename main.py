
import itertools
import os
import random
import re
import sys
import traceback

import tweepy
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv('TWEET_API_BEARER_TOKEN')

client = tweepy.Client(bearer_token=BEARER_TOKEN)

def windows(iterable, length=2, overlap=0):
    it = iter(iterable)
    results = list(itertools.islice(it, length))
    while len(results) == length:
        yield results
        results = results[length-overlap:]
        results.extend(itertools.islice(it, length-overlap))

def build_structure(string):
    return [' '.join(window) for n in range(len(string)) for
            window in windows(string.split(), n + 1, n)]

def clean_word(string):
    pattern = re.compile('[\W_]+')
    words = []
    for word in string.split():
        word = re.sub(pattern, ' ', word)
        words.append(word)
    return ' '.join(words)

def make_keywords(string, minLength = 1, maxLength = 3):
    string = clean_word(string.lower())
    keywords = []
    for phrase in build_structure(string):
        if len(list(phrase.split())) >= minLength and len(list(phrase.split())) <= minLength:
            if phrase is not None and phrase.strip() != '':
                keywords.append(phrase)
    return random.choice(keywords)

def clean_tweets(tweet):
    processed_text = re.sub(r"(?:RT \@|http?\://|https?\://|www|#|\:|\@)\S+", "", tweet)
    processed_text = " ".join(processed_text.split())

    return processed_text

def fetch_tweets(query, next_token = None):
    tweets = client.search_recent_tweets(query=query, next_token=next_token)
    return tweets

def fetch_result(keyword):
    tweets = []
    reps = []

    tweets = fetch_tweets(make_keywords(keyword) + ' lang:id')
    
    if tweets.data is None:
        tweets = fetch_tweets(make_keywords(keyword, 1, 1) + ' lang:id')


    for t in tweets.data:
        replies = fetch_tweets(f'in_reply_to_status_id:{t.id} lang:id')
        if replies.data is not None:
            for r in replies.data:
                reps.append(r.text)
        
        if len(reps) >= 4:
            break;       
    

    if len(reps) >= 1:
        return '🌻 ' + random.choice(reps)
    else:
        if tweets.data is not None:
            rng = random.choice(tweets.data)
            return '🔥 ' + rng.text
        else:
            return 'not found'

def main():    
    question = input('>  ')

    while (question != 'quit'):
        try:
            print(clean_tweets(fetch_result(question)).lower())
            question = input('>  ')
        except Exception as e:
            print(traceback.format_exc())
            sys.exit(0)


if __name__ == '__main__':
    main()