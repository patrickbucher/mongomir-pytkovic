#!/usr/bin/env python3

import falcon
import logging
import os

class QuoteResource:
    def __init__(self):
        self.logger = logging.getLogger('Quote')
        self.logger.setLevel(logging.DEBUG)
        logdir = os.environ['LOGDIR'] 
        logpath = os.path.join(logdir, 'falcon.log')
        fh = logging.FileHandler(logpath)
        self.logger.addHandler(fh)

    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }
        self.logger.debug('GET on /quote')
        resp.media = quote

api = falcon.API()
api.add_route('/quote', QuoteResource())
