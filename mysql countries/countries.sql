SELECT countries.region, COUNT(*) FROM countries
GROUP BY countries.region
ORDER BY COUNT(*) DESC