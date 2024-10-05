SELECT day
FROM (
    SELECT
        day,
        price,
        LAG(price) OVER (ORDER BY day) AS prev_price,
        LEAD(price) OVER (ORDER BY day) AS next_price
    FROM prices
) AS sub
WHERE prev_price IS NOT NULL
  AND next_price IS NOT NULL
  AND price > prev_price
  AND price > next_price
ORDER BY day;
