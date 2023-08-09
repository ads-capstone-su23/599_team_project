USE 599_capstone;

DROP TABLE IF EXISTS nar_temp;
DROP TABLE IF EXISTS news_articles_rvsd;

/**/
CREATE TABLE news_articles_rvsd
(
text_id INT UNSIGNED AUTO_INCREMENT,
source_name VARCHAR(1000),
author VARCHAR(1000),
title VARCHAR(1000),
url VARCHAR(1000),
publish_date VARCHAR(30),
article_text LONGTEXT,
content LONGTEXT,
CONSTRAINT pk_text_id PRIMARY KEY (text_id)
);
DESC news_articles_rvsd;

/**/
CREATE TABLE nar_temp
(
source_name VARCHAR(1000),
author VARCHAR(1000),
title VARCHAR(1000),
url VARCHAR(1000),
publish_date VARCHAR(30),
content LONGTEXT
);
DESC nar_temp;
