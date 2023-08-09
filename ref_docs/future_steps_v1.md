Future steps
Data Ops
. collect more data, incl. expanding source list to include more tradtional newspaper outlets, as well as regional and local news sources 
. refine scraping process
. perform additional cleaning steps, including automating it, say even using ML methods
. implement cloud storage and triggering
. expand database schemas to include business-realted data, such as customer info, usage details, etc.

Modeling
. look at an addtional add-on for finding articles that cover unique-find issues that haven't hit mainstream yet.
. explore additional classification methods, including multiclass-multilable prediction
. explore on-the-fly TM to over-time expand topics
. explore more advanced (NN-based) topic modeling, such as BERTopic
. add recommender system (colloborative filtering) once enough people use the system, to avoid cold-start*
. dervive an internal labeled sentiment dataset, much like PerSenT, by crowd-sourcing scraped articles
. explore word embeddings further
. refine threshold calculations

Evaluating
. consider how to better deal with very subjectively good news, which is based leanings on hot-button issues. cows and ducks swimming together seems like good news, but Trump getting reelected will only be positive for a sgement of the population.
. A/B testing
. perform further statistical analysis to determine why RoBERTa differs from BERT for this particular data


* this is a biggie. i would also note that a goal is not to achieve an "echo-chamber" system that sends people to only news they agree with.