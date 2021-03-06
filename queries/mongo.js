db.matches.findOne({
  "home_players.name": "Sinan Bolat"
}, {
  "home_players.$id": 1
}).home_players[0].birthday

db.matches.findOne({
  "away_players.name": "Sinan Bolat"
}, {
  "away_players.$id": 1
}).away_players[0].birthday

db.matches.aggregate([{
  $group: {
    _id: "$league_id",
    total: {
      $sum: 1
    }
  }
}])

db.matches.aggregate([{
    $lookup: {
      from: "leagues",
      localField: "league_id",
      foreignField: "id",
      as: "matches_league"
    }
  },
  {
    "$project": {
      "_id": 0,
      "date": 1,
      "date_timestamp": 1,
      "matches_league.league": 1,
      "matches_league.country": 1,
      "round": 1,
      "home_team": 1,
      "home_goals": 1,
      "away_team": 1,
      "away_goals": 1,
      "home_players": 1,
      "away_players": 1
    }
  },
  {
    "$match": {
      "$or": [{
          "home_players.name": "Sinan Bolat"
        },
        {
          "aways_players.name": "Sinan Bolat"
        }
      ]
    }
  },
  {
    "$sort": {
      date_timestamp: -1
    }
  }
])