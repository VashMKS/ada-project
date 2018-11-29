# TODO

## Questions

- Can or can we not use libraries in the cluster via egg files? If so, how?
- Rob suggested the LIWC as a list of words to use as sentiment analysis classifier, but can't seem to find anything resembling a list of words.

## Data Retrieval

- Should we work with a subset of the data?
- How do we sample it?
- Streamline use of the cluster (egg files?). Create a pipeline to make it easy for us to submit jobs to it.

## Data Exploration

- Several metrics (number of communities, users, etc)
- Similarity between communities
- Clustering
- Topics

## NLP / Text Processing

- Libraries to look up: [spaCy](https://spacy.io/), [TextBlob](https://textblob.readthedocs.io/en/dev/), [nltk](https://www.nltk.org/), [Standford core NLP](https://stanfordnlp.github.io/CoreNLP/)
- [Libaries](https://github.com/shuyo/language-detection) to filter out only English comments
- [encoding?](https://www.reddit.com/r/redditdev/comments/178mk1/praw_encoding_question/)
- Tokenization (spaCy, nltk)
- We have TONS of data, casefolding is not needed
- Should we do stemming? Lots of comments are written by non-native English speakers and thus include a lot of mistakes, yet again our dataset is big. Stemming would cause loss of information, so probably not.
- Same question but with lemmatization. It is quite complex and we don't have the time to do it properly.
- Can we use bag of words to make data lighter? Do APIs accept that?
- The data comes from social media, even though usually Reddit elaborates more than Twitter users we will still have a ton of common slang expressions (ikr, smh, iirc, etc).
- Should we use n-grams? Of what length? n=5 beats neural networks but this absolutely blows up our space... Maybe bigrams are fine for concepts such as "United States", which is relevant to the topic at hand. Maybe it's better to do feature selection?

## Echo Metrics

- Our metrics should measure how much of an echo chamber a community (subredit) is by looking at the comments on it.
- Come up with a few metrics (after the study)
- Come up with a list of potential known echo chambers and non echo chambers (subjective?) to serve as test set
- Test the performance of the metrics in our test set and
- Come up with nice names for them :D

## Presentation

- Web for the Data Story [here](https://project-echo-chamber.github.io/)
- Needed graphs (clustering, PCA, data metrics, etc)
- Craft a collection of links and references
- Use Rob's image of hell in presentation 11 to talk about this project
