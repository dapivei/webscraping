#!/usr/bin/python
# -*- coding: utf-8 -*-


# =========== Código para scrapear tweets empleando GetOldTweets3 ==============
#
# Objetivo: con este código se scrapea tweets, más o menos recientes de @nperedo.
#
# Notas: idealmente quisiéramos scrapear tweets recientes de todos los usuarios;
# \sin embargo, para ello se requiere una cuenta de developper en Tweepy. Por lo
# \para el presente ejercicio se realiza el scrapeo con GetOldTweets3.
#
# Output: el output de este script es un documento .csv
# ==============================================================================

# ===================== Importando paquetería empleanda ========================

import GetOldTweets3 as got
import pandas as pd

username = 'nperedo'                         # set username of interest
since_date = '2019-01-20'                    # set daterange
until_date = '2020-05-02'                    # set daterange
count = 1000                                 # setcount max of tweets

tweetCriteria = got.manager.TweetCriteria().setUsername(username).setSince(since_date).setUntil(until_date)# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

# Creating list of chosen tweet data
user_tweets = [[tweet.date, tweet.text] for tweet in tweets]

df = pd.DataFrame(data=user_tweets,
                    columns=['date_time', "tweet"])
df['date'] = df['date_time'].dt.date
df['time'] = df['date_time'].dt.time


file_name="tweet_search"                    # define name of file
df.to_csv(file_name, sep='\t')              # save output in .csv file
