from __future__ import absolute_import, unicode_literals

from collections import namedtuple

import requests

API_URL = "http://api.forismatic.com/api/1.0/"

Quote = namedtuple("Quote", ["text", "author"])


def read_quote(id=None):
    params = {"method": "getQuote", "format": "json", "lang": "en"}
    if id:
        params["key"] = id

    response = requests.get(API_URL, params).json()
    return Quote(response["quoteText"], response["quoteAuthor"])
