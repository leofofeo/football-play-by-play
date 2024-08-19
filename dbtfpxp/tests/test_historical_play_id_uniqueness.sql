select
    historical_play_id,
    count(*) as record_count
from football_play_by_play.staging."src_historical_play_by_play"
group by historical_play_id
having  count(*) > 1