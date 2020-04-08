-- github.com/balajisomasale

SELECT 
    COUNT(CITY) - COUNT(DISTINCT CITY)
FROM
    STATION;
