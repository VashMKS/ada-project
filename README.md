# An Overview on the Echo-chamber Effect

## Abstract
Has the high connectivity that came with the internet made us better? Is it fostering healthy discussion and debate between the different communities or is the echo-chamber effect predominant and we are actually becoming more divided and reinforcing our biases?
https://en.wikipedia.org/wiki/Echo_chamber_(media)

Reddit is the "frontpage of the internet" (13 years online, more than half a billion monthly users, top 3 most visited website in the US and top 20 in the world). It's developers have been open about the huge amount of information that flows around the site and the responsibility it takes to handle such a social outlet. We will make use of the dataset containing reddit comments, which should make up for a pretty good uncensored dataset on the interaction of the different communities.

Our goal is to have a good picture of how a particular technology (the internet no less) is shaping debate and in consequence, society. This is really important since big challenges lie ahead of our generation: climate change, the rise of populism or the increasing inequality, both between nations and inside their borders, just to give a few examples. Fake news and crafted narratives have been a hot topic for a while, and while the internet has given certain agents the ability to reach a lot of people with minimal effort it has also provided huge advancements just for the sheer fact that sharing information and knowledge is easier than ever in history. Hence, understanding the way in which we communicate through that vast network is key in order to come up with ways to protect ourselves from bad actors that might try to influence our reasoning.

## Research questions
What is the echo-chamber effect? How can we measure it?
Does it have a stronger effect on certain topics? Does the size of a community influence it? What about other factors?
Over time, do communities eventually overcome the effect or does it get worse? Under which conditions?
Can we fight it? How?

## Dataset
We plan on using the Reddit comments dataset. It contains all of reddit's comments from its inception and up to March 2017. Reddit already has a rich structure and we plan to take advantage of it. We are going to focus on subreddits, as those are going to be our communities. Since we also have user data we can watch for cross-interaction between subreddits, brigadding, trolls, bots, etc.
This is basically a list of 53,851,542 JSON objects with comments using the following structure:

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

Specifically, we plan to mainly use the username, subreddit id, and timestamp. As the project unfolds we might make use of controversiality, downvotes, score, etc in order to go more in depth (if time allows).

Some speedbumps we might find are dead subreddits and known bots posting useless comments, we might have to work a bit if we want to clean the dataset perfectly but it looks mostly solid. The good thing about reddit is that there's probably about a thousand good resources we can find online for such a task.

Size-wise we might also encounter some roadblocks since this is a pretty big dataset. If we find that it's too much to handle we might resort to shrinking substantially, which thanks to the good structure can be done easily.

## A list of internal milestones up until project milestone 2
- Get familiar with the phenomenon of the echo-chamber, find sources and references
- Set the foundations of our study using well-known concepts from graph and network theory

## Questions for TAa
This a pretty broad and complex subject. Given that we 'only' have 2 months time, how deep would we need to go in order to have an acceptable result?
