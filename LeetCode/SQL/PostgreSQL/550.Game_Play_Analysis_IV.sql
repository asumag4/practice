SELECT 
    ROUND(
        (
            1.0 * COUNT(DISTINCT player_id) /
            (
                SELECT 
                    COUNT(DISTINCT a2.player_id)
                FROM Activity a2
            )
        ),
        2
    ) AS Fraction
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT 
        a1.player_id,
        MIN(a1.event_date) + 1
    FROM Activity a1
    GROUP BY a1.player_id
);