SELECT
  age_bucket
  ,ROUND(
    (SUM(ts.time_spent_send) 
      / SUM(ts.time_spent_open + ts.time_spent_send)
      ) 
    * 100, 2) AS send_prc
  -- ,ts.time_spent_open / (ts.time_spent_open + ts.time_spent_send)
  ,ROUND(
    (SUM(ts.time_spent_open) 
      / SUM(ts.time_spent_open + ts.time_spent_send)
      ) 
    * 100, 2) AS open_prc
FROM 
(SELECT
  user_id
-- sending vs. opening snaps (as a percentage of total time spent on these activities)
  ,SUM(
    CASE 
      WHEN activity_type = 'open'
      THEN time_spent
      ELSE 0
    END
  )  AS time_spent_open
  ,SUM(
    CASE 
      WHEN activity_type = 'send'
      THEN time_spent
      ELSE 0
    END
  )  AS time_spent_send
FROM activities
GROUP BY user_id) ts -- time_spend
JOIN age_breakdown ab 
  ON ts.user_id = ab.user_id
GROUP BY age_bucket

-- group by age group