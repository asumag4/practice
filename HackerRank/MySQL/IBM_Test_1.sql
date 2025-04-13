SELECT 
    c.name AS city_name,
    SUM(s.duration) AS total_duration
FROM 
    CITIES c
JOIN 
    CLIENTS cl ON c.id = cl.city_id
JOIN 
    SESSIONS s ON cl.id = s.client_id
GROUP BY 
    c.name
ORDER BY 
    total_duration ASC;