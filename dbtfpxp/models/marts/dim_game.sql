with dim_game AS (
    select * from FOOTBALL_PLAY_BY_PLAY.staging."src_historical_play_by_play"
)
select 
    distinct game_id,
    season_type,
    season,
    week,
    game_date,
    stadium,
    weather,
    home_team,
    away_team,
    home_score,
    away_score,
    location,
    result AS home_point_differential,
    total AS total_points_scored,
    spread_line AS closing_spread_line,
    total_line AS closing_total_line
from dim_game
