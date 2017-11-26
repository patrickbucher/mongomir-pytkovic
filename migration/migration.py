#!/usr/bin/env python3

import sqlite3
import os
from datetime import datetime

cursor = None

def extract_players(prefix, cursor, row):
    players = []
    for i in range(1, 12):
        field = prefix + str(i)
        player_id = row[field]
        # TODO use cursor to fetch player name and birthday
        players.append(player_id)
    return players

def to_match_dict(cursor, row):
    match = {}
    full_league = row['league']
    match['league'] = full_league[full_league.index(' '):].strip()
    match['country'] = full_league[:full_league.index(' ')].strip()
    match['season'] = row['season']
    match_datetime = datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
    match['date'] = match_datetime.strftime('%d.%m.%Y')
    match['round'] = row['stage']
    match['home_team'] = row['home_team_name'].encode('utf-8')
    match['away_team'] = row['away_team_name'].encode('utf-8')
    match['home_goals'] = row['home_team_goal']
    match['away_goals'] = row['away_team_goal']
    match['home_players'] = extract_players('hp', cursor, row)
    match['away_players'] = extract_players('ap', cursor, row)
    return match

def get_match_query():
    return """
        select Match.id, league.name as league, season, stage, date,
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
        join League on (Match.league_id = League.id)
        join Team home_team on (Match.home_team_api_id = home_team.team_api_id)
        join Team away_team on (Match.away_team_api_id = away_team.team_api_id)
        where not home_player_1 is null and not away_player_1 is null
        order by league_id asc, stage asc;
    """

def main():
    datdir = os.environ['DATDIR']
    db = os.path.join(datdir, 'database.sqlite')
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    matches = []
    for row in cursor.execute(get_match_query()):
        match = to_match_dict(cursor, row)
        matches.append(match)

    print(matches)

if __name__ == '__main__':
    main()
