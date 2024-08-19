SELECT *
FROM football_play_by_play.staging."src_historical_play_by_play"
WHERE (pass_play = TRUE AND rush_play = TRUE) OR (pass_play = FALSE AND rush_play = FALSE);
