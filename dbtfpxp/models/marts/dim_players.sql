with dim_players as (
    select 
        distinct player_id,
        player_name,
        COALESCE(passer_player_id, rusher_player_id, receiver_player_id, interception_player_id) AS player_id,
        COALESCE(passer_player_name, rusher_player_name, receiver_player_name, interception_player_name) AS player_name,
        jersey_number,
        position -- Can be derived based on player role or by adding a manual mapping
    from football_play_by_play.staging."src_historical_play_by_play"
    unpivot(
        player_id, player_name for role in (
        passer_player_id, passer_player_name,
        rusher_player_id, rusher_player_name,
        receiver_player_id, receiver_player_name,
        interception_player_id, interception_player_name))
)
select * from dim_players
