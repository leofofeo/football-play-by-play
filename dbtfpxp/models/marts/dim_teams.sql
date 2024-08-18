with dim_teams as (
    select * from football_play_by_play.staging."src_historical_play_by_play"
)
SELECT DISTINCT
    COALESCE(posteam, defteam) AS team_id,
    CASE WHEN posteam IS NOT NULL THEN 'possession' ELSE 'defense' END AS team_type,
    home_team,
    away_team,
    location,
    home_coach,
    away_coach,
    stadium,
    roof,
    surface
FROM dim_teams
