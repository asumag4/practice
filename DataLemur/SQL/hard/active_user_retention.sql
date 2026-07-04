WITH july_users AS (
  SELECT
    DISTINCT
      user_id
  FROM user_actions
  WHERE event_date >= '2022-07-01'
    AND event_date < '2022-08-1'
    AND event_type IN ('sign-in','like','comment')
)
  
,august_users AS (
  SELECT
    DISTINCT
      user_id
  FROM user_actions
  WHERE event_date >= '2022-06-01'
    AND event_date < '2022-07-1'
    AND event_type IN ('sign-in','like','comment')
)

SELECT
  7                   AS month
  ,COUNT(ju.user_id)  AS monthly_active_users
FROM july_users     ju
JOIN august_users   au ON au.user_id = ju.user_id