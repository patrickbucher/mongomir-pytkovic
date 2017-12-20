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

class CorsMiddleware():
    def process_request(self, request, response):
        response.set_header('Access-Control-Allow-Origin', 'http://localhost:8001')

class MatchResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        logger.debug('GET on /api/match')
        name = req.get_param('name')
        resp.media = pprint.pformat(list(mongo_db.matches.aggregate([
            {"$lookup": {
                "from": "leagues",
                "localField": "league_id",
                "foreignField": "id",
                "as": "matches_league"
            }},
            {"$project": {
                "_id": 0,
                "date": 1,
                "date_timestamp": 1,
                "matches_league.league": 1,
                "matches_league.country": 1,
                "round": 1,
                "home_goals": 1,
                "away_goals": 1,
                "home_players": 1,
                "away_players": 1
            }},
            {"$match": {
                "$or": [{"home_players.name" : name}, {"away_players.name": name}]
            }},
            {"$sort": {"date_timestamp": -1}}
        ])))

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

api = falcon.API(middleware=[CorsMiddleware()])
api.add_route('/api/match', MatchResource())
api.add_route('/api/stats', StatsResource())
