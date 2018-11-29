# TODO

## Questions

- Can or can we not use libraries in the cluster via egg files? If so, how?

## Data Retrieval

- Should we work with a subset of the data?
- How do we sample it?
- Streamline use of the cluster

## Data Exploration

- Several metrics (number of communities, users, etc)
- Similarity between communities
- Clustering
- Topics

## NLP / Text Processing

- filter out only English comments [language detection libaries](https://github.com/shuyo/language-detection)
- [encoding?](https://www.reddit.com/r/redditdev/comments/178mk1/praw_encoding_question/)
- Tokenization (spaCy, nltk)
- We have TONS of data, casefolding is not needed
- Should we do stemming or lemmatization? Lots of comments are written by non-native English speakers and thus include a lot of mistakes, yet again our dataset is big. Both stemming and lemmatization would cause loss of information, so probably not. Also, lemmatization is quite complex and we don't have the time to do it properly.
- Can we use bag of words to make data lighter? Do APIs accept that?
- The data comes from social media, even though usually Reddit elaborates more than Twitter users we will still have a ton of common expressions (ikr, smh, iirc, etc).
- Should we use n-grams? Of what length? n=5 beats neural networks but this absolutely blows up our space... Maybe bigrams are fine for concepts such as "United States", which is relevant to the topic at hand. Maybe it's better to do feature selection?

## Echo Metrics

- Come up with a few metrics (after the study)
- Come up with nice names for them :D

## Presentation

- Web for the Data Story [here](https://project-echo-chamber.github.io/)
- Needed graphs (clustering, PCA, data metrics, etc)
- Craft a collection of links and references
