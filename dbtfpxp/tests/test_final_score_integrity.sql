SELECT
    game_id,
    home_score,
    away_score,
    result,
    (home_score - away_score) AS calculated_result
FROM
    football_play_by_play.staging."src_historical_play_by_play"
WHERE
    result != (home_score - away_score)
