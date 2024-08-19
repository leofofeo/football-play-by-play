SELECT roof
FROM football_play_by_play.staging."src_historical_play_by_play"
WHERE roof NOT IN ('dome', 'outdoors', 'closed', 'open');