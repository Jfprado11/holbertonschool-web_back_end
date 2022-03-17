-- mysql Advanced
-- geting by lo9ng a metal abdn
SELECT band_name, IFNULL(split, 2020) - formed as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
