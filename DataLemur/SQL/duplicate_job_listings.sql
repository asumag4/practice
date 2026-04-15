SELECT
  COUNT(1)            AS duplicate_companies
FROM 
  (
  SELECT
    COUNT(1)          AS count_dupes
    -- ,company
  FROM job_listings
  GROUP BY 
    company_id
    ,title
    ,description
  )
  duplicates
WHERE duplicates.count_dupes > 1