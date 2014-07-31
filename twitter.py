__author__ = 'robin'

import tweepy, re


class Twitter:
    APP_KEY = 'Qz2XQ5KJL5jhQC8dlxxY3MbIl'
    APP_SECRET = 'YE0iJo6Pf6ojiZu1KREChjW5e9wNOoldtHOrhRh3DDPvjn7W3L'
    ACCESS_TOKEN = None
    auth = None

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.APP_KEY, self.APP_SECRET)

    def get_user_timeline(self, user, pages):
        api = tweepy.API(self.auth)

        tweets = []
        for page in range(1, pages+1):
            tweets.append(api.user_timeline(screen_name=user, page=page))

        return sum(tweets, [])

    def get_timeline_entities(self, user, pages=1):
        return [t.entities for t in self.get_user_timeline(user, pages)]

    def get_timeline_urls(self, entities):
        all_urls = []
        for t in entities:
            urls = [e['display_url'] for e in t['urls']]
            all_urls.append(urls)
        return all_urls

    def get_urls_that_match(self, pattern, entities, escape=True):
        all_urls = []
        if escape:
            pattern = re.escape(pattern)
        for urls in self.get_timeline_urls(entities):
            filtered = [url for url in urls if re.match(pattern, url)]
            all_urls.append(filtered)

        return sum(all_urls, [])







