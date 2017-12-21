#!/usr/bin/env python3

import sqlite3
from pymongo import MongoClient
import os
from datetime import datetime
import time

# SQLite connection and setup
datdir = os.environ['DATDIR']
sqlite_db = os.path.join(datdir, 'database.sqlite')
connection = sqlite3.connect(sqlite_db)
connection.row_factory = sqlite3.Row

# MongoDB connection and setup
client = MongoClient()
mongo_db = client.soccer
mongo_db.matches.remove({})
mongo_db.leagues.remove({})

def main():
    all_players = load_all_players()

    n_matches = 0
    for row in connection.cursor().execute(get_match_query()):
        match = to_match_dict(row, all_players)
        matches = mongo_db.matches
        match_id = matches.insert_one(match).inserted_id
        n_matches = n_matches + 1
        print('inserted match as', match_id, 'into MongoDB')

    league_query = 'select id, name from League'
    n_leagues = 0
    for row in connection.cursor().execute(league_query):
        league = to_league_dict(row)
        leagues = mongo_db.leagues
        league_id = leagues.insert_one(league).inserted_id
        n_leagues = n_leagues + 1
        print('inserted league as', league_id, 'into MongoDB')

    print('done, inserted %d matches and %d leagues' % (n_matches, n_leagues))

def load_all_players():
    players = {}
    players_query = """
        select player_api_id as id, player_name as name, birthday
        from Player
    """
    cursor = connection.cursor()
    for row in cursor.execute(players_query):
        id = int(row['id'])
        name = row['name'].replace("'", '’')
        birthday = to_date_str(row['birthday'])
        players[id] = {'name': name, 'birthday': birthday}

    return players

def to_match_dict(row, all_players):
    match = {}
    match['league_id'] = row['league_id']
    match['season'] = row['season']
    date_str = to_date_str(row['date'])
    match['date'] = date_str
    match['date_timestamp'] = to_timestamp(date_str)
    match['round'] = row['stage']
    match['home_team'] = row['home_team_name']
    match['away_team'] = row['away_team_name']
    match['home_goals'] = row['home_team_goal']
    match['away_goals'] = row['away_team_goal']
    match['home_players'] = extract_players('hp', row, all_players)
    match['away_players'] = extract_players('ap', row, all_players)
    return match

def to_league_dict(row):
    league = {}
    # the league name contains the country
    country_league = split_league_name(row['name'])
    league['id'] = row['id']
    league['league'] = country_league[0]
    league['country'] = country_league[1]
    return league

def extract_players(prefix, match_row, all_players):
    match_players = []
    for i in range(1, 12):
        player = {}
        field = prefix + str(i)
        player_id_str = match_row[field]
        if player_id_str != None:
            player_id = int(player_id_str)
            player = all_players[player_id]
            if player != None:
                match_players.append(player)

    return match_players

def get_match_query():
    return """
        select Match.id, league_id, season, stage, date,
        home_team.team_long_name as home_team_name, home_team.team_short_name,
        away_team.team_long_name as away_team_name, away_team.team_short_name,
        home_team_api_id, away_team_api_id, home_team_goal, away_team_goal,
        home_player_1 as hp1, home_player_2 as hp2, home_player_3 as hp3,
        home_player_4 as hp4, home_player_5 as hp5, home_player_6 as hp6,
        home_player_7 as hp7, home_player_8 as hp8, home_player_9 as hp9,
        home_player_10 as hp10, home_player_11 as hp11,
        away_player_1 as ap1, away_player_2 as ap2, away_player_3 as ap3,
        away_player_4 as ap4, away_player_5 as ap5, away_player_6 as ap6,
        away_player_7 as ap7, away_player_8 as ap8, away_player_9 as ap9,
        away_player_10 as ap10, away_player_11 as ap11
        from Match
        join Team home_team on (Match.home_team_api_id = home_team.team_api_id)
        join Team away_team on (Match.away_team_api_id = away_team.team_api_id)
        where not home_player_1 is null and not away_player_1 is null
        order by league_id asc, stage asc;
    """

def to_date_str(datetime_str):
    dt = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
    return dt.strftime('%d.%m.%Y')

def to_timestamp(date_str):
    dt = datetime.strptime(date_str, '%d.%m.%Y')
    return time.mktime(dt.timetuple())

def split_league_name(country_league):
    split = country_league.index(' ')
    country = country_league[split:].strip()
    league = country_league[:split].strip()
    return (country, league)


if __name__ == '__main__':
    main()
