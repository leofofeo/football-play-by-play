create or replace table marts.fact_game_summary as (
select
    g.game_id,
    g.season,
    g.week,
    g.home_team,
    g.away_team,
    g.game_date,
    sum(case when p.touchdown then 1 else 0 end) as total_touchdowns,
    SUM(coalesce(try_to_number(p.yards_gained, 0), 0)) AS total_yards_gained,
    sum(case when p.pass_attempt then 1 else 0 end) as total_pass_attempts,
    sum(case when p.rush_attempt then 1 else 0 end) as total_rush_attempts,
    SUM(coalesce(try_to_number(d.drive_play_count, 0), 0)) AS total_plays,
    SUM(coalesce(try_to_number(d.drive_first_downs, 0), 0)) AS total_first_downs,
    AVG(coalesce(try_to_number(p.expected_points_added, 0), 0)) AS avg_epa
from fact_plays p
join fact_drives d on p.game_id = d.game_id
join dim_games g on p.game_id = g.game_id
group by g.game_id, g.season, g.week, g.home_team, g.away_team, g.game_date
);