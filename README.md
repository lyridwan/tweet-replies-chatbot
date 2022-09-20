# Tweet-replies-chatbot
Simple chatbot that uses [Twitter](https://twitter.com/)' replies as "the source of knowledge".
It uses [Tweepy](https://www.tweepy.org/) lib for accessing the Twitter API.

The bot's responses are, most of the time, incoherent or, sometime, offensive.

How to run this thing?
---------------------- 
1. Copy and/or rename `.env.example` to `.env`
2. Paste your Twitter API bearer token to `TWEET_API_BEARER_TOKEN` variable on `.env` file
3. From the command-line:
```
    $ python main.py
    
    >  Pagi gan
    🌻 pagii ngap, semangat jugaa!💪🤍
    >  Apa kabar?
    🔥 apa kabar dari bali menyapa ?
    >  Saya sedang bahagia
    🌻 pendongeng handal jugaa nih
    >  Cuaca sekarang
    🌻 mw ujan tapi panas
```
Credits
----------------------
This project is heavily inspired by [botgan](https://github.com/geovedi/botgan)
