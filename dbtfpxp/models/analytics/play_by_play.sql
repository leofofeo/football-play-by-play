with play_by_play as (
    select * from football_play_by_play.staging.src_historical_play_by_play
)
select 
    *
from play_by_play