#!/usr/bin/env python3

import falcon
from pymongo import MongoClient
import logging
import os
import pprint

client = MongoClient()
mongo_db = client.soccer
logger = logging.getLogger('Match')
logger.setLevel(logging.DEBUG)
logdir = os.environ['LOGDIR']
logpath = os.path.join(logdir, 'falcon.log')
fh = logging.FileHandler(logpath)
logger.addHandler(fh)

class MatchResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        logger.debug('GET on /api/match')
        resp.media = pprint.pformat(mongo_db.matches.find_one())

class StatsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        logger.debug('GET on /api/stats')
        resp.media = pprint.pformat(list(mongo_db.matches.aggregate([{
            "$group": {
                "_id": "$league_id",
                "total": {
                    "$sum": 1
                }
            }
        }])))

api = falcon.API()
api.add_route('/api/match', MatchResource())
api.add_route('/api/stats', StatsResource())
