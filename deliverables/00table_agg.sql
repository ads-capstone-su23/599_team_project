USE 599_capstone;

SELECT * FROM nar_temp;
SELECT * FROM news_articles
LIMIT 100000;

SELECT * FROM news_articles
LIMIT 10000;

SELECT * FROM news_articles
WHERE source_name NOT IN ("CNN", "The Washington Post", "Fox News", "Breitbart News");

SELECT * FROM news_articles
WHERE LEFT(url, 21) = 'https://theeagleswire'
LIMIT 10000;

SELECT
source_name,
COUNT(*) AS source_count,
COUNT(*) / sum(count(*)) over () AS source_dist
FROM news_articles
GROUP BY source_name;

SELECT DISTINCT source_name, title, article_text, content, url
FROM news_articles
WHERE article_text IS NOT NULL
LIMIT 10000;

SELECT
source_name,
COUNT(*) AS source_count,
COUNT(*) / sum(count(*)) over () AS source_dist
FROM news_articles
WHERE article_text IS NOT NULL
GROUP BY source_name WITH ROLLUP;

SELECT
source_name,
COUNT(*) AS source_count,
COUNT(*) / sum(count(*)) over () AS source_dist
FROM news_articles
WHERE article_text IS NULL
GROUP BY source_name WITH ROLLUP;

SELECT source_name, title, article_text
FROM news_articles
WHERE article_text IS NULL
LIMIT 100000;

SELECT DISTINCT url
FROM news_articles
WHERE article_text IS NULL
LIMIT 100000;

DESC news_articles;

SELECT
source_name,
CAST(LEFT(publish_date, 10) AS DATE) AS date,
COUNT(*) AS source_count,
COUNT(*) / sum(count(*)) over () AS source_dist
FROM news_articles
WHERE CAST(LEFT(publish_date, 10) AS DATE) <= '2023-06-19'
GROUP BY source_name, CAST(LEFT(publish_date, 10) AS DATE) with rollup
ORDER BY CAST(LEFT(publish_date, 10) AS DATE), source_name;
