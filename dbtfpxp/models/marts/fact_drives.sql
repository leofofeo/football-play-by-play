create or replace view marts.fact_drives as
SELECT
    game_id,
    drive,
    possession_team AS team_id,
    start_time AS drive_start_time,
    drive_time_of_possession,
    drive_play_count,
    drive_first_downs,
    drive_yards_penalized,
    drive_start_yard_line,
    drive_end_yard_line,
    drive_quarter_start,
    drive_quarter_end,
    drive_ended_with_score
FROM staging.src_historical_play_by_play
GROUP BY
    game_id, drive, possession_team, start_time,
    drive_time_of_possession, drive_play_count,
    drive_first_downs, drive_yards_penalized,
    drive_start_yard_line, drive_end_yard_line,
    drive_quarter_start, drive_quarter_end, drive_ended_with_score
;