
- CNN, Fox News, and the New York Times are the most neutral news outlets based on their last 100 tweets.

- CBS and the BBC are on the other side of the spectrum, being the most positive news outlets with CBS being very positive.

- The Vader analysis conducted is highly subject to what the user wishes to tweet on a particular day. Although each outlet has a specific reputation, the analysis doesn't fall in line with the reputation.

- Given the fast moving and global nature of news, 100 tweets doesn't seem to be a large sample size. Expanding the tweet sample would be very beneficial.


```python
import tweepy
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import time
from datetime import datetime
import seaborn as sns
from config import consumer_key, consumer_secret, access_token, access_token_secret
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```


```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```


```python
results_list = []

target_users = ("@BBC", "@CBS", "@CNN", "@FoxNews", "@NYTimes")
```


```python
for user in target_users:
    counter = 0
    public_tweets = api.user_timeline(user, count = 100)

    for tweet in public_tweets:
        compound = analyzer.polarity_scores(tweet["text"])["compound"]
        pos = analyzer.polarity_scores(tweet["text"])["pos"]
        neu = analyzer.polarity_scores(tweet["text"])["neu"]
        neg = analyzer.polarity_scores(tweet["text"])["neg"]
        tweets_ago = counter
        tweet_text = tweet["text"]

        results_list.append({"User" : user,
                           "Date": tweet["created_at"],
                           "Compound" : compound,
                           "Positive" : pos,
                           "Negative" : neg,
                           "Neutral" : neu,
                           "Count" : counter,
                           "Tweet Text" : tweet_text})
        
        counter = counter + 1
```


```python
df = pd.DataFrame(results_list)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Compound</th>
      <th>Count</th>
      <th>Date</th>
      <th>Negative</th>
      <th>Neutral</th>
      <th>Positive</th>
      <th>Tweet Text</th>
      <th>User</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0000</td>
      <td>0</td>
      <td>Tue Jun 26 21:20:15 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>RT @BBC6Music: Did @kanyewest and @theweeknd "...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.0000</td>
      <td>1</td>
      <td>Tue Jun 26 19:05:08 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>😎🔥🍦 Hot temperatures in the UK are expected to...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.2960</td>
      <td>2</td>
      <td>Tue Jun 26 18:03:06 +0000 2018</td>
      <td>0.074</td>
      <td>0.792</td>
      <td>0.134</td>
      <td>Tonight, @itsanitarani and @bbcnickrobinson as...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0000</td>
      <td>3</td>
      <td>Tue Jun 26 17:02:02 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>How would you feel if the builder only made yo...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0000</td>
      <td>4</td>
      <td>Tue Jun 26 16:33:41 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>RT @bbcwritersroom: Tomorrow, Wednesday 27th J...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0000</td>
      <td>5</td>
      <td>Tue Jun 26 16:00:15 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>🍅 You can grow tomatoes in Iceland?!   https:/...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.0000</td>
      <td>6</td>
      <td>Tue Jun 26 14:52:03 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>RT @BBCWales: #ToProvideAllPeople: A star-stud...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.8360</td>
      <td>7</td>
      <td>Tue Jun 26 14:32:33 +0000 2018</td>
      <td>0.000</td>
      <td>0.683</td>
      <td>0.317</td>
      <td>RT @BBCRadio2: To celebrate the anniversary of...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.6114</td>
      <td>8</td>
      <td>Tue Jun 26 13:12:16 +0000 2018</td>
      <td>0.000</td>
      <td>0.818</td>
      <td>0.182</td>
      <td>RT @BBCR1: Happy Birthday, @ArianaGrande! 🎈✨\n...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.0000</td>
      <td>9</td>
      <td>Tue Jun 26 12:58:04 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>🚄😽🎀 Japan has unveiled a pink bullet train the...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.5267</td>
      <td>10</td>
      <td>Tue Jun 26 12:02:04 +0000 2018</td>
      <td>0.000</td>
      <td>0.673</td>
      <td>0.327</td>
      <td>Activist\nPoet\nDirector\nActor\nWriter...\n\n...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.0000</td>
      <td>11</td>
      <td>Tue Jun 26 11:02:03 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>🍕💐 Would you say 'I dough' to this pizza bouqu...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.0000</td>
      <td>12</td>
      <td>Tue Jun 26 09:30:00 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>🌍♻️💥👊\nWhat will your #PlasticsAction be? http...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>13</th>
      <td>-0.2732</td>
      <td>13</td>
      <td>Tue Jun 26 08:00:16 +0000 2018</td>
      <td>0.139</td>
      <td>0.861</td>
      <td>0.000</td>
      <td>Turns out you're biased in all sorts of ways y...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>14</th>
      <td>-0.7717</td>
      <td>14</td>
      <td>Tue Jun 26 07:26:08 +0000 2018</td>
      <td>0.295</td>
      <td>0.705</td>
      <td>0.000</td>
      <td>Seabirds are starving to death on the remote L...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.5994</td>
      <td>15</td>
      <td>Tue Jun 26 07:00:12 +0000 2018</td>
      <td>0.000</td>
      <td>0.738</td>
      <td>0.262</td>
      <td>💕 Julie is the childcare champion in the heart...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.3612</td>
      <td>16</td>
      <td>Mon Jun 25 18:03:04 +0000 2018</td>
      <td>0.000</td>
      <td>0.815</td>
      <td>0.185</td>
      <td>✨ These women are ditching their straighteners...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.0000</td>
      <td>17</td>
      <td>Mon Jun 25 17:31:08 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Two teams of junior doctors from teaching hosp...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.2732</td>
      <td>18</td>
      <td>Mon Jun 25 16:02:03 +0000 2018</td>
      <td>0.000</td>
      <td>0.769</td>
      <td>0.231</td>
      <td>🙌😂 Well, that escalated quickly.\n#HearHer #Li...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>19</th>
      <td>-0.5524</td>
      <td>19</td>
      <td>Mon Jun 25 15:01:34 +0000 2018</td>
      <td>0.229</td>
      <td>0.771</td>
      <td>0.000</td>
      <td>RT @BBCTwo: SO much tension between Louis and ...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.3182</td>
      <td>20</td>
      <td>Mon Jun 25 14:57:32 +0000 2018</td>
      <td>0.000</td>
      <td>0.839</td>
      <td>0.161</td>
      <td>RT @BBCTwo: brb just gonna pop inside for some...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.5423</td>
      <td>21</td>
      <td>Mon Jun 25 13:48:41 +0000 2018</td>
      <td>0.000</td>
      <td>0.836</td>
      <td>0.164</td>
      <td>RT @bbcarts: If you’re from the North this wil...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.6360</td>
      <td>22</td>
      <td>Mon Jun 25 13:03:07 +0000 2018</td>
      <td>0.000</td>
      <td>0.656</td>
      <td>0.344</td>
      <td>🐶😍 They're all beautiful in our eyes! \n#World...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.5719</td>
      <td>23</td>
      <td>Mon Jun 25 12:04:05 +0000 2018</td>
      <td>0.000</td>
      <td>0.802</td>
      <td>0.198</td>
      <td>🙌💪 @ChelseaClinton says it's time we rethink g...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.3400</td>
      <td>24</td>
      <td>Mon Jun 25 11:01:03 +0000 2018</td>
      <td>0.104</td>
      <td>0.741</td>
      <td>0.156</td>
      <td>📖✨🌲 From the Forbidden Forest at Hogwarts to P...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.0000</td>
      <td>25</td>
      <td>Mon Jun 25 10:12:49 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>🌋 Lava from Hawaii's Kilauea volcano creeps cl...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>26</th>
      <td>-0.4215</td>
      <td>26</td>
      <td>Mon Jun 25 08:03:05 +0000 2018</td>
      <td>0.128</td>
      <td>0.872</td>
      <td>0.000</td>
      <td>This headteacher is budgeting to buy hygiene p...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0.0000</td>
      <td>27</td>
      <td>Mon Jun 25 07:26:06 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>🤖 What does it mean for AI to have a soul?\n👉 ...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>28</th>
      <td>-0.6486</td>
      <td>28</td>
      <td>Mon Jun 25 07:00:13 +0000 2018</td>
      <td>0.301</td>
      <td>0.699</td>
      <td>0.000</td>
      <td>Should we bring the woolly mammoth back from t...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.0000</td>
      <td>29</td>
      <td>Sun Jun 24 19:03:02 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Follow the inner workings of @nytimes, one of ...</td>
      <td>@BBC</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>470</th>
      <td>0.0000</td>
      <td>70</td>
      <td>Tue Jun 26 14:18:06 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>RT @taffyakner: I went to the woods because I ...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>471</th>
      <td>0.0000</td>
      <td>71</td>
      <td>Tue Jun 26 14:10:34 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>When Pedro Cabrita Reis became an internationa...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>472</th>
      <td>0.5859</td>
      <td>72</td>
      <td>Tue Jun 26 14:00:14 +0000 2018</td>
      <td>0.000</td>
      <td>0.840</td>
      <td>0.160</td>
      <td>Denmark takes on France, and needs a win or dr...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>473</th>
      <td>-0.2263</td>
      <td>73</td>
      <td>Tue Jun 26 13:45:06 +0000 2018</td>
      <td>0.091</td>
      <td>0.909</td>
      <td>0.000</td>
      <td>A judge threw out a lawsuit brought by San Fra...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>474</th>
      <td>0.0000</td>
      <td>74</td>
      <td>Tue Jun 26 13:31:54 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>President Trump has often lauded Harley-Davids...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>475</th>
      <td>-0.4215</td>
      <td>75</td>
      <td>Tue Jun 26 13:30:08 +0000 2018</td>
      <td>0.214</td>
      <td>0.677</td>
      <td>0.109</td>
      <td>“Who is this stupid God?" The remarks of Presi...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>476</th>
      <td>0.4404</td>
      <td>76</td>
      <td>Tue Jun 26 13:15:02 +0000 2018</td>
      <td>0.000</td>
      <td>0.868</td>
      <td>0.132</td>
      <td>Lindsay Lohan is turning 32 in July. For the f...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>477</th>
      <td>0.0000</td>
      <td>77</td>
      <td>Tue Jun 26 13:00:12 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Morning Briefing: Here's what you need to know...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>478</th>
      <td>0.0000</td>
      <td>78</td>
      <td>Tue Jun 26 12:45:06 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>A new version of the 1040 income tax form may ...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>479</th>
      <td>0.0772</td>
      <td>79</td>
      <td>Tue Jun 26 12:15:08 +0000 2018</td>
      <td>0.093</td>
      <td>0.802</td>
      <td>0.105</td>
      <td>Technology is fast changing how people with di...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>480</th>
      <td>0.0000</td>
      <td>80</td>
      <td>Tue Jun 26 12:00:06 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>This item is the most frequently found type of...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>481</th>
      <td>-0.3400</td>
      <td>81</td>
      <td>Tue Jun 26 11:45:06 +0000 2018</td>
      <td>0.112</td>
      <td>0.888</td>
      <td>0.000</td>
      <td>So far, the Pawnee Fire has burned thousands o...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>482</th>
      <td>-0.2960</td>
      <td>82</td>
      <td>Tue Jun 26 11:30:13 +0000 2018</td>
      <td>0.104</td>
      <td>0.896</td>
      <td>0.000</td>
      <td>No heat. Leaks. Mold and pests. New York City ...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>483</th>
      <td>0.0000</td>
      <td>83</td>
      <td>Tue Jun 26 11:30:12 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Jimmy Fallon responds to President Trump: "You...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>484</th>
      <td>0.0000</td>
      <td>84</td>
      <td>Tue Jun 26 11:15:09 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>A New York Times investigation found that preg...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>485</th>
      <td>0.0000</td>
      <td>85</td>
      <td>Tue Jun 26 11:14:04 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>RT @andrewkeh: There are hundreds of thousands...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>486</th>
      <td>0.0772</td>
      <td>86</td>
      <td>Tue Jun 26 11:00:03 +0000 2018</td>
      <td>0.000</td>
      <td>0.947</td>
      <td>0.053</td>
      <td>“I see mothers bury their sons,” Antwon Rose I...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>487</th>
      <td>0.0000</td>
      <td>87</td>
      <td>Tue Jun 26 10:45:05 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>The group stage of the World Cup is almost ove...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>488</th>
      <td>-0.2263</td>
      <td>88</td>
      <td>Tue Jun 26 10:30:07 +0000 2018</td>
      <td>0.226</td>
      <td>0.584</td>
      <td>0.191</td>
      <td>A rift in the Democratic party has opened over...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>489</th>
      <td>0.0000</td>
      <td>89</td>
      <td>Tue Jun 26 10:15:06 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Here are a few things to watch out for today a...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>490</th>
      <td>0.0000</td>
      <td>90</td>
      <td>Tue Jun 26 10:00:08 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Morning Briefing: Here's what you need to know...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>491</th>
      <td>-0.6486</td>
      <td>91</td>
      <td>Tue Jun 26 09:45:03 +0000 2018</td>
      <td>0.223</td>
      <td>0.777</td>
      <td>0.000</td>
      <td>A video showed a woman in California unleashin...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>492</th>
      <td>0.0000</td>
      <td>92</td>
      <td>Tue Jun 26 09:40:05 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Who, exactly, is ISIS? That question fuels our...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>493</th>
      <td>0.0000</td>
      <td>93</td>
      <td>Tue Jun 26 09:15:05 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Sometimes spiders ride the wind https://t.co/A...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>494</th>
      <td>-0.5574</td>
      <td>94</td>
      <td>Tue Jun 26 09:00:07 +0000 2018</td>
      <td>0.267</td>
      <td>0.644</td>
      <td>0.089</td>
      <td>The latest discontented group to upset the Chi...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>495</th>
      <td>-0.3875</td>
      <td>95</td>
      <td>Tue Jun 26 08:43:52 +0000 2018</td>
      <td>0.134</td>
      <td>0.866</td>
      <td>0.000</td>
      <td>"I don't know how it works and I don't care. N...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>496</th>
      <td>-0.2500</td>
      <td>96</td>
      <td>Tue Jun 26 08:27:06 +0000 2018</td>
      <td>0.111</td>
      <td>0.889</td>
      <td>0.000</td>
      <td>Erdogan must now face Turkey's troubled econom...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>497</th>
      <td>0.0000</td>
      <td>97</td>
      <td>Tue Jun 26 08:18:42 +0000 2018</td>
      <td>0.000</td>
      <td>1.000</td>
      <td>0.000</td>
      <td>Hedge funds and private-equity firms are pouri...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>498</th>
      <td>0.7579</td>
      <td>98</td>
      <td>Tue Jun 26 08:02:04 +0000 2018</td>
      <td>0.000</td>
      <td>0.764</td>
      <td>0.236</td>
      <td>A Sri Lankan port is one of the most vivid exa...</td>
      <td>@NYTimes</td>
    </tr>
    <tr>
      <th>499</th>
      <td>-0.7184</td>
      <td>99</td>
      <td>Tue Jun 26 07:46:02 +0000 2018</td>
      <td>0.250</td>
      <td>0.750</td>
      <td>0.000</td>
      <td>RT @nytimesworld: Turkey is facing an array of...</td>
      <td>@NYTimes</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 8 columns</p>
</div>




```python
df.to_csv("Twitter_News_Mood.csv", index=False)
```


```python
for user in target_users:
    dataframe = df.loc[df["User"] == user]
    plt.scatter(dataframe["Count"],dataframe["Compound"],label = user)
    

plt.legend(bbox_to_anchor = (1,1))
plt.title("Sentiment Analysis of Media Tweets (6/26/2018)")
plt.xlabel("Count")
plt.ylabel("Tweet Polarity")
plt.xlim(-1, 101)
plt.grid()

plt.savefig("Sentiment Analysis of Media Tweets")
plt.show()
```


![png](output_7_0.png)



```python
average_sentiment = df.groupby("User")["Compound"].mean()
average_sentiment
```




    User
    @BBC        0.144648
    @CBS        0.339176
    @CNN       -0.102103
    @FoxNews    0.082498
    @NYTimes   -0.055879
    Name: Compound, dtype: float64




```python
x_axis = np.arange(len(average_sentiment))
xlabels = average_sentiment.index
count = 0
for sentiment in average_sentiment:
    plt.text(count, sentiment+.01, str(round(sentiment,2)))
    count = count + 1
plt.bar(x_axis, average_sentiment, tick_label = xlabels, color = ['silver', 'b', 'y', 'g', 'c'])

plt.title("Overall Sentiment of Media Tweets (6/26/2018)")
plt.xlabel("New Organizations")
plt.ylabel("Tweet Polarity")
plt.savefig("Overall Sentiment of Media Tweets")
plt.show()
```


![png](output_9_0.png)

