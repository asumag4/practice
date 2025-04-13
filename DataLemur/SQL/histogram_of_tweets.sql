SELECT
-- 5. Select the count  
  t.count AS tweet_bucket,
-- 6. Aggregate the count of `user_id` for each count of tweets `t.count`
  COUNT(user_id) AS users_num
FROM (
  SELECT 
--   1. Select the `user_id`
    user_id,
    -- 2. Aggregate the count of `user_id`
    COUNT(user_id) AS count
  FROM tweets
--   3. As specified by the question; select only 2022 year
  WHERE EXTRACT(YEAR FROM tweet_date) = 2022
-- 4. Group By `user_id`
  GROUP BY user_id) 
  AS t
-- 7. Make sure to `GROUP BY` t.count 
GROUP BY t.count
