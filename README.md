# An Overview on the Echo-chamber Effect

## Abstract
Has the high connectivity that came with the internet made us better? Is it fostering healthy discussion and debate between the different communities or is the echo-chamber effect predominant and we are actually becoming more divided?

Reddit is the "frontpage of the internet" (give some stats about reddit, user count, etc). It's developers have been open about the huge amount of information that flows around the site (more stats) and have always tried to keep up with the public's interest and to not fold to external biases (net neutrality?). That should make up for a pretty good uncensored dataset on the interaction of the different communities.

## Research questions
Is the echo-chamber effect real? If so, how can we measure it?
Does it have a stronger effect on certain topics? 
Over time, do communities eventually overcome the effect or does it get worse? Under which condition?
Does it have a bigger effect on big or small communities?
Can we fight it? How?

## Dataset
We plan on using the Reddit comments dataset. It is basically a list of 53,851,542 comments with the following structure:

{
   "gilded":0,
   "author_flair_text":"Male",
   "author_flair_css_class":"male",
   "retrieved_on":1425124228,
   "ups":3,
   "subreddit_id":"t5_2s30g",
   "edited":false,
   "controversiality":0,
   "parent_id":"t1_cnapn0k",
   "subreddit":"AskMen",
   "body":"content",
   "created_utc":"1420070668",
   "downs":0,
   "score":3,
   "author":"TheDukeofEtown",
   "archived":false,
   "distinguished":null,
   "id":"cnasd6x",
   "score_hidden":false,
   "name":"t1_cnasd6x",
   "link_id":"t3_2qyhmp"
}

It contains all of reddit's comments from its inception and up to March 2017. Reddit already has a rich structure and we plan to take advantage of it. We are going to focus on subreddits, as those are the communities of reddit. Since we also have user data we can watch for cross-interaction between subreddits, brigadding, trolls, etc. 
Specifically, we plan to mainly use the username, subreddit id, and timestamp. As the project unfolds we might make use of controversiality, downvotes, score, etc in order to go more in depth.

List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

## A list of internal milestones up until project milestone 2
- Get familiar with the phenomenon, find sources
- Set the foundations of our study using well-known concepts from graph and network theory

## Questions for TAa
This a pretty broad and complex subject. Given that we 'only' have 2 months time, how deep would we need to go in order to have an acceptable result?

topics that we could research:
- the battle for net neutrality
- the US 2016 election coverage (aka russian trolls)
- the evolution of whistleblowing and it's perception by the public (see Assange, Snowden, Wikileaks, etc) although cannot analyze khashoggi's case unless we retrieve the data ourselves, which is a possibility
- r/ProjectDiscovery and crowdsourced science

platform ideas:
Github pages?
upon finishing the project make a post in r/dataisbeautiful
with our results (see https://www.reddit.com/r/dataisbeautiful/comments/9sny2t/growth_of_subreddits/)

links of interest:
https://www.tableau.com/
