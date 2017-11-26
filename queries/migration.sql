select id, league_id, season, stage, date,
home_team_api_id, away_team_api_id, home_team_goal, away_team_goal,
home_player_1 as hp01, home_player_2 as hp02, home_player_3 as hp03,
home_player_4 as hp04, home_player_5 as hp05, home_player_6 as hp06,
home_player_7 as hp07, home_player_8 as hp08, home_player_9 as hp9,
home_player_10 as hp10, home_player_11 as hp11,
away_player_1 as ap01, away_player_2 as ap02, away_player_3 as ap03,
away_player_4 as ap04, away_player_5 as ap05, away_player_6 as ap06,
away_player_7 as ap07, away_player_8 as ap08, away_player_9 as ap09,
away_player_10 as ap10, away_player_11 as ap11
from Match
where not home_player_1 is null and not away_player_1 is null
order by league_id asc, stage asc;
