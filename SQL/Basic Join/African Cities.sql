-- github.com/balajisomasale

SELECT CITY.NAME 
FROM CITY, COUNTRY
WHERE CITY.COUNTRYCODE = COUNTRY.CODE AND COUNTRY.CONTINENT = 'Africa';
