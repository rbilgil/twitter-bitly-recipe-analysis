__author__ = 'robin'

import requests
import json


class Bitly:

    ACCESS_TOKEN = '9a473872655297f727c063076badd8a18b0833e0'
    endpoints = {
        'clicks': 'https://api-ssl.bitly.com/v3/link/clicks',
        'countries': 'https://api-ssl.bitly.com/v3/link/countries',
        'refer': 'https://api-ssl.bitly.com/v3/link/referrers',
    }

    def get_link_data(self, link):

        if link.find('http') == -1:
            link = 'http://' + link

        query_params = {'access_token': self.ACCESS_TOKEN,
                        'link': link}

        data = {}
        for name, endpoint in self.endpoints.iteritems():
            response = requests.get(endpoint, params=query_params, verify=False)
            data[name] = json.loads(response.content)

        return data

