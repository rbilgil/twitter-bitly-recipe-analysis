__author__ = 'robin'

from twitter import Twitter
from bitly import Bitly

bit = Bitly()

tw = Twitter()

entities = tw.get_timeline_entities('bbcgoodfood', pages=1)
links = tw.get_urls_that_match('bit.ly', entities, escape=False)

clicks = {}
for link in links:
    data = bit.get_link_data(link)
    print data



