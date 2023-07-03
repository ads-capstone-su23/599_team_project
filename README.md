# News Curation - Unlocking Positive News Through Language Models
Daily Retreat: Using Sentiment Analysis to Find, Personalize and Share Positive News from Popular Online Sources

#### -- Programming Languages/Platforms: Python, Jupyter Notebooks, MySQL
#### -- Project Status: [Active]

## Goals
* Develop a pipeline to extract positive/uplifting news articles from usual news sources like CNN, Fox, MSN, New York Times, etc.

## Team Members
* Azucena Faus
* Dave Friesen
* Aaron Carr


## Methods Used
* Data Collection: NewsAPI/Webscraping
* Exploratory data analysis (EDA)
* Text data preprocessing (e.g., normalization, tokenization)
* Term frequency-inverse document frequency (TF-IDF) vectorization
* Sentiment Analysis
* Topic Modeling
* Text classification
  

## Overview

In today's fast-paced digital world, the constant influx of news – especially news with highly negative content – can be distracting and even detrimental to mental health (Blades, 2021). Simultaneously, manually sifting and curating positive or even "silver-lining" news stories requires intentionality and is tedious and time-consuming. As many news consumers may also view some negative news to be necessary - for example, "hard" information like timely, impactful, and current events is reality - many sources will continue to provide hard news of all valances, positive or negative. However, herein lies an opportunity to curate positive and personalized news that meets (exceeds) consumer topic and timing preferences.


## Selected Dataset:

NewsAPI content from news sources considered popular and/or mainstream in the U.S.

## Description of Dataset (data source, number of variables, size of dataset, etc.): 

Similar to the text mining project developed by Carr et al. (2023) for ADS-509, Team 9 will be using the NewsAPI REST Application Programming Interface (API) to access news content from a variety of “current and historic news articles published by over 80,000 worldwide sources” (NewsAPI, n.d.). However, the content and source focus has changed from collecting content from politically biased sources for bias classification to the most popular and/or mainstream sources toward a different problem statement.

We will use two identified references to generate a list of potential source content, to obtain content that will appeal to the largest segmentation of U.S. news readers interested in highly positive articles (Shearer & Mitchell, 2021; Statista, n.d.). We will be using the paid version of the API, which potentially has pre-scraped content from each article; for any instance where the content is not readily available, scraping will be done to close the gaps.

The NewsAPI returns a JSON object with multiple items. This project will mainly focus on collecting three features for this project, including `content` (which is unstructured), `URL,` and `category,` along with an engineered feature for storage of data we must scrape ourselves. While we do not have a target number of articles, we will collect as many as possible in the allowable time frame. *Note*: The paid API version allows for 250,000 requests per month, so the main limitations will be based on how much content must be scraped manually.


## Purpose and Expected Value

The present study aims to demonstrate the automated delivery of positive news highlights with optional topic personalization. This service will be accomplished through applied Natural Language Processing (NLP) and a prototype, leveraging advanced language modeling techniques across a wide corpus of news media sources.

"So-called good news outlets" report "surprisingly large audiences and increasing engagement" (McIntyre & Gibson, 2016). The authors note that trends suggest media executives are seeking to increase their audience by emphasizing positives in the news (McIntyre & Gibson, 2016). While this opportunity may be niche relative to much current-event hard news, this study and prototype aim to capitalize on trends in upbeat, topical news delivery.

## Literature Review

There is a general consensus that news consumption is detrimental to the physical and mental wellness of readers (McLaughlin et al., 2022). This is due to the negative aspects of news media that makes it lucrative and "click-able," but damaging to individuals. 

There is also a growing trend in people that seek out positive news stories (McIntyre & Gibson, 2016). The article by McIntyre and Gibson mention how more popular news sources are encouraging writers to focus on the "silver lining" to a news story, in order to promote and access this growing trend in reader preferences.

As to the topic of news curation, there have been systems developed using NLP methods like topic-modeling and sentiment analysis, that curate the news based on topic, as in COVID-19, or topics selected by a user (Surahman et al., 2022). However, there is currently no system in place that seeks to curate news from reliable already existing news sources, to focus on positive stories.

Using similar methodologies to topical news curation, this project seeks to remedy the maladies of constant negative newsfeeds and provide positive news content for a growing number of individuals that seek a retreat from usual news stories.

## Motivation

We are motivated by an interest in automated information curation - in this example, based on news valance and corpora - and by the accelerating potential and opportunities in Natural Language Processing (even if only semantic search, not generative). Some estimate as much as 90% of the Internet-enabled world's data is unstructured, which, combined with language model capability growth, emphasizes a significant opportunity to “unlock” information and knowledge (MIT Sloan School of Management, 2022). This project allows us to step into the accelerating NLP and language model opportunity.

## Working Hypothesis 

The existence of objective idealism has been debated since the time of Plato (Trodden, 2018). However, today it is generally accepted that the manifestation of such objectivity remains very theoretical and that when attempting to examine the actual output of human thought, there are naturally elements of subjectivity. Beginning in the 1960s, a definition and attempted application of objectivity in terms of news reporting was related to maintaining journalistic professional judgments, while at the same time eliminating any of the reporters’ personal opinions (Pressman, 2018). Consequently, by this assumption, the application of this type of objectivity will still result in specific human sentiments–specifically, articles will  “contain information about emotion, mood, or feelings” of the reporter (Albrecht et al., 2021).

Based on this, the project’s working hypothesis is that sentiment analysis (SA) techniques can be implemented to clearly determine the overall sentiment of articles relative to concepts covered, specifically in terms of positive and negative emotions conveyed. Moreover, it is hypothesized that the signals achievable for positive sentiment (in terms of sentiment score) will represent relatively strong indications of which articles reflect reporting of uplifting (or “feel-good”) content.

## Data Science Objectives

In order to address the stated business problem, several data science objectives have been identified in order to ultimately develop a highly effective SA machine learning (ML) model that can be applied to collected news source articles.
1. Build an automated, systematic, and deployment-ready pipeline for the ingestion, preprocessing, modeling, and evaluation of text-based data.
2. Apply topic modeling techniques to produce class labels for specific documents (articles) within the dataset.
3. Use SA ML modeling to output a “positivity” score for every article.

## Planned Methodology 

To achieve the business and data science objectives, the following methods will be used:
1. Collect data, via API call (supplemented with web scraping, as needed).
2. Perform Exploratory Data Analyses (EDA) to investigate underlying structures of the data, which will include generation of descriptive statistics and visualizations (e.g., word count box plots, histograms, word clouds, etc.).
3. Perform text data preprocessing using methods tailored to the specific content source. This may include removing any items considered noise, such as stop words and punctuation, as well as examining whether lemmatization or stemming methods would bolster model performance.
4. Perform topic modeling to create instance labels via unsupervised methods, possibly using both simple (NMF) and complex (NN-based transfer learning).
5. Apply SA modeling methods to achieve “positivity” assignment per article.
6. Evaluate SA performance by applying the trained model to an independent, similar, and sentiment-labeled dataset, such as the PerSenT dataset from Bastan et al. (2020).
7. Serve up examples of uplifting content based on chosen categories/topics.
8. Rate sources based on proportion of positive and negative content.

## Real-World Impact and Planned Deliverables

The real-world impact of this study involves going against the grain of usual recommender systems that strengthen the proliferation of negative or scandalous news stories to users. These systems leave their readers at risk of forming a “maladaptive relationship with the news,” that results in mental and physical ills for those individuals (McLaughlin et al., 2022). This solution is a balanced departure from the addiction to negative news exposure and the removal of news altogether (which has its own negative outcomes for society). 

The final deliverable will be the first step towards implementing a “mental health” plug-in that will curate a customer’s newsfeed with positive and uplifting news. This will help increase faith in humanity for these users while decreasing anxiety (Suttie, 2018). 

Specifically, the deliverable will be a pipeline that will provide positive news for the day in real-time.

## Additional Comments / Roadblocks

Some possible roadblocks:
There is the risk of a limited dataset in terms of size; especially if there is a need to webscrape a great number of news articles due to the NewsAPI content limitations.
This dataset might be limited in diversity, if there is a search criteria requirement; such search keywords will limit the types of articles that will be analyzed.






## References
* Albrecht, J., Ramachandran, S., & Winkler, C. (2021). Blueprints for text analytics using Python: Machine learning-based solutions for common real world (NLP) applications.     O’Reilly.
* Bastan, M. (2020, October 29). PerSenT [Data set and code book]. GitHub. Retrieved July 1, 2023 from https://github.com/MHDBST/PerSenT
* Bastan, M., Koupaee, M., Son, Y., Sicoli, R., & Balasubramanian, N. (2020). Author’s sentiment prediction. ArXiv. https://doi.org/10.48550/arXiv.2011.06128
* Blades, R. (2021). Protecting the brain against bad news. Canadian Medical Association Journal, 193(12), E428-E429. https://doi.org/10.1503%2Fcmaj.1095928
* Guo, L., Vargo, C. J., Pan, Z., Ding, W., & Ishwar, P. (2016). Big Social Data Analytics in Journalism and Mass Communication: Comparing Dictionary-Based Text Analysis and Unsupervised Topic Modeling. Journalism & Mass Communication Quarterly, 93(2), 332–359. https://doi.org/10.1177/1077699016639231
* Khandelwal, D., Shanbhag, D., Shriyan, A., Thorve, R., & Borse, Y. (2018). LeMeNo: Personalised News Using Machine Learning. 2018 Fourth International Conference on Computing Communication Control and Automation (ICCUBEA) (pp. 1-4), Pune, India. https://doi.org/10.1109/ICCUBEA.2018.8697560
* McIntyre, K. E., & Gibson, R. (2016). Positive news makes readers feel good: A "silver-lining" approach to negative news can attract audiences. Southern Communication Journal, 81(5), 304-315. https://www.tandfonline.com/doi/full/10.1080/1041794X.2016.1171892
* McLaughlin, B., Gotlieb, M. R., & Mills, D. J. (2022, August 23). Caught in a Dangerous World: Problematic News Consumption and Its Relationship to Mental and Physical Ill-Being. Taylor & Francis Online. https://doi.org/10.1080/10410236.2022.2106086
* MIT Sloan School of Management (2022, April 10). Tapping the power of unstructured data. MIT Sloan School of Management. https://mitsloan.mit.edu/ideas-made-to-matter/tapping-power-unstructured-data
* NewsAPI. (n.d.). Search worldwide news with code. Retrieved June 5, 2023 from https://newsapi.org/
* Pressman, M. (2018, November 2018). Journalistic objectivity evolved the way it did for a reason. Time.  https://time.com/5443351/journalism-objectivity-history/
* Shearer, E., & Mitchell, A. (2021, May 7). Broad agreement in U.S. – even among partisans – on which news outlets are part of the ‘mainstream media’. Pew Research Center. https://www.pewresearch.org/short-reads/2021/05/07/broad-agreement-in-u-s-even-among-partisans-on-which-news-outlets-are-part-of-the-mainstream-media/
* Statista. (n.d.). Leading global English-language news websites in the United States in February 2023, by monthly visits. Retrieved July 1, 2023 from https://www.statista.com/statistics/381569/leading-news-and-media-sites-usa-by-share-of-visits/
* Surahman, E., Liao, Y.-C., Lin, Y.-C., & She, E. (2022). Digital news transformation on education in the most affected country by COVID-19 using the Topic Modeling and Sentiment Analysis. 2022 8th International Conference on Education and Technology (ICET), 99–106. https://doi.org/10.1109/ICET56879.2022.9990686
* Suttie, J. (2018, August 28). Five Ways to Restore Your Faith in Humanity. Greater Good Magazine Science-Based Insights for a Meaningful life. https://greatergood.berkeley.edu/article/item/five_ways_to_restore_your_faith_in_humanity
* Trodden, A. (2018, March 21). What is objective and subjective idealism, what are the differences? TostPost.  https://tostpost.com/news-and-society/7947-what-is-objective-and-subjective-idealism-what-are-the-differences.html
