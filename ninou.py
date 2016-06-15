#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import time
import tweepy

consumer_key = "xoxoxoxoxo" # CONSUMMER KEY
consumer_secret = "xoxoxoxoxo" # CONSUMMER SECRET
access_key = "xoxoxoxoxo" # ACCESS TOKEN
access_secret = "xoxoxoxoxo" # ACCESS TOKEN SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        me = API.me()
        me = me.id
        user_id = status.author.id
        if user_id == me:
            print("Je vais pas me bloquer non plus, je veux bien être une sous race, mais quand même...")
        else:
            twitter_user = api.get_user(id = user_id)
            user_name = twitter_user.screen_name
            print(status.text)
            print(twitter_user.screen_name)
            try:
                api.create_block(id = user_id)
            except:
                print("Erreur, le blocage de @%s a échoué" % (user_name))
            else:
                print("@%s a été bloqué avec succès" % (user_name))

    def on_error(self, status_code):
        if status_code == 420:
            print("Attends un peu, t'as dépassé la limite autorisée par l'API. Reviens dans 15 minutes")
        else:
            status_code = str(status_code)
            print ('Erreur ' + status_code)
            return True

    def on_timeout(self):
        print ('/!\ Connexion perdue /!\ ')
        return True

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['Ninou'])
