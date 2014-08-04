__author__ = 'robin'

from twitter import Twitter
from bitly import Bitly
import pymongo

bit = Bitly()
tw = Twitter()
client = pymongo.MongoClient()


handles = [
    'bbcgoodfood'
]

file_names = ['clicks.csv', 'countries.csv', 'referrers.csv']

entities = tw.get_timeline_entities(handles[0], pages=1)
links = tw.get_urls_that_match('bit.ly', entities, escape=False)

for link in links:
    data = bit.get_link_data(link)
    for file_name in file_names:
        try:
            with open(file_name, 'w') as file:
                writer = csv.writer(file, dialect='excel')
                writer.writerow(data[file_name.replace('.csv', '')])
        except IOError as ioe:
            print 'Error: ' + str(ioe)



