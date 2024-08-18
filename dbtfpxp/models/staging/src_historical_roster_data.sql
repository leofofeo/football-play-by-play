with src_historical_roster_data as (
    select * from football_play_by_play.raw."HISTORICAL-ROSTER-DATA-CSV-STREAM"
)
select player_name, year, team
from src_historical_play_by_play