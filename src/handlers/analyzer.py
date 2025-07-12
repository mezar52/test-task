def select_top_tweet(tweets):
    """
    Picks the tweet with the highest total engagement (likes + retweets).
    """
    return max(tweets, key=lambda t: t['likes'] + t['retweets'])