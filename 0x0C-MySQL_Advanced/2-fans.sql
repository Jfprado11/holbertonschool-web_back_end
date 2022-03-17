-- Mysql Adavanced
-- using a craete table to check the bands
SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
