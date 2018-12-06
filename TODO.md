# TODO

## Questions

- Can or can we not use libraries in the cluster via [egg files](https://stackoverflow.com/questions/2026395/how-to-create-python-egg-file)? If so, how? [Tutorial on Mattermost](https://mrtopf.de/en/a-small-introduction-to-python-eggs/)
- Rob suggested the LIWC as a list of words to use as sentiment analysis classifier, but can't seem to find anything resembling a list of words.

## Data Retrieval (Vik)

- Should we work with a subset of the data? Take year 2016 and early 2017 as dataset
- How do we sample it? make a random sample of maybe 1% to test our algorithms locally. If we can use eggs then run them in all the data, otherwise stick to the sample. In the later case maybe we can still create the graph by retrieving the right info for its creation to local.
- Streamline use of the cluster (egg files?). Create a pipeline to make it easy for us to submit jobs to it.
- Filter by size (minimum nº comments, minimum nº active users), language (only take English comments, it's easier on our NLP libraries).

## Data Exploration (All)

- Several metrics (number of communities, nº users both in Reddit and per Community, etc)
- Similarity between communities?
- Clustering?
- Topic detection: try to find better classifier, right now it's very basic

## NLP / Text Processing (Jorge)

- Libraries to look up: [spaCy](https://spacy.io/), [TextBlob](https://textblob.readthedocs.io/en/dev/), [nltk](https://www.nltk.org/) (and using [vader](http://www.nltk.org/howto/sentiment.html) with it for sentiment analysis), [Standford core NLP](https://stanfordnlp.github.io/CoreNLP/)
- [Libaries](https://github.com/shuyo/language-detection) to filter out only English comments
- [encoding?](https://www.reddit.com/r/redditdev/comments/178mk1/praw_encoding_question/)
- Tokenization (spaCy, nltk)
- We have TONS of data, casefolding, stemming, lemmatization, slang removal, etc is not needed
  - Should we do stemming? Lots of comments are written by non-native English speakers and thus include a lot of mistakes, yet again our dataset is big. Stemming would cause loss of information, so probably not.
  - Same question but with lemmatization. It is quite complex and we don't have the time to do it properly.
- Can we use bag of words to make data lighter? Do APIs accept that? No need, we got the cluster.
- The data comes from social media, even though usually Reddit elaborates more than Twitter users we will still have a ton of common slang expressions (ikr, smh, iirc, etc).
- Should we use n-grams? Of what length? n=5 beats neural networks but this absolutely blows up our space... Maybe bigrams are fine for concepts such as "United States", which is relevant to the topic at hand. Maybe it's better to do feature selection?

## Echo Metrics (Dídac)

- Our metrics should measure how much of an echo chamber a community (subredit) is by looking at the comments on it.
- Come up with a few metrics (after data exploration)
- Come up with a list of potential known echo chambers and non echo chambers (subjective?) to serve as test set
- Test the performance of the metrics in our test set and try to use them to find new echo chambers
- Come up with cool names for the metrics

- First approach: per community basis
  - we study some metrics of Reddit comments (controversiality, polarity, subjectivity). Then create metrics by adding the relevant ones.
  - after that, test the heuristic metrics in our subreddit test set

- Second approach: via the whole network
  - Craft the Reddit Graph (TM): each community is a node, 2 nodes are connected if a certain number of users are active in both communities, edges are thicker the more users are cross-posting between the communities, we can colour the edges using codes (maybe green/red shades for general sentiment of the connection).
  - Use it to study how isolated communities are and use that as a metric for echo chambering (possibly combined with the previous approach)



## Presentation (Dídac)

- Web for the [data story](https://project-echo-chamber.github.io/)
- Nice [example](https://dlab.epfl.ch/2017-08-30-of-sheep-and-beer/)
- Needed graphs (clustering, PCA, data metrics, etc)
- Section about methodology
- Craft a collection of links and references
- Use Rob's image of hell in presentation 11 to talk about this project


## Skeleton of the final Report/Data Story

#### Introduction
- Abstract
- What is Reddit?
- What is the Echo Chamber Effect
- The dataset
  - Explain the dataset and the subset we decided to use, give some basic stats about it (size in terms of nº of communities, nº active users, etc). Here's the [2016 official Reddit report]()

#### Exploring Reddit
- Methodology
- Basic Metrics
  - Polarity
  - Subjectivity
  - others
- The Reddit Graph (TM)

#### Finding Echo Chambers

#### Conclusion
