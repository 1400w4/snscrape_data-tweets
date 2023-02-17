import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "ChatGPT lang:id until:2023-02-17 since:2022-11-30"
tweets = []
limit = 5000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    # print(vars(tweet))
    # break

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

dataframe = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(dataframe)

dataframe.to_csv('test_data_twitter.csv')