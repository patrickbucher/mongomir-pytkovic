#!/usr/bin/env python3

import falcon
from pymongo import MongoClient
import logging
import os
import pprint

client = MongoClient()
mongo_db = client.soccer

class MatchResource:
    def __init__(self):
        self.logger = logging.getLogger('Match')
        self.logger.setLevel(logging.DEBUG)
        logdir = os.environ['LOGDIR'] 
        logpath = os.path.join(logdir, 'falcon.log')
        fh = logging.FileHandler(logpath)
        self.logger.addHandler(fh)

    def on_get(self, req, resp):
        """Handles GET requests"""
        self.logger.debug('GET on /match')
        resp.media = pprint.pformat(mongo_db.matches.find_one(), indent = 4)

api = falcon.API()
api.add_route('/api/match', MatchResource())
