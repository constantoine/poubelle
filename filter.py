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
API = tweepy.API(auth)

me = API.me()
me = me.id

liste_de_followers = (me,)

erreur_limite_atteinte = " \n \n /!\ Trop de requêtes dans le même quart d'heure. C'est pas ma faute, c'est Twitter qui limite les requêtes. Le programme continuera de fonctionner, mais aucun des tweets contenant le mot que vous recherchez qui sera tweeté dans les 15 prochaines minutes ne pourra être affiché par le programme, le temps que la limite saute /!\ \n \n "

def limite_API(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print(erreur_limite_atteinte)
            time.sleep(15 * 61)

for follower in limite_API(tweepy.Cursor(API.followers).items()):
    id_follower = follower.id
    liste_de_followers = liste_de_followers + (id_follower,)

print(liste_de_followers)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        user_id = status.author.id
        user_name = status.user.screen_name
        texte_du_tweet = status.text
        if user_id in liste_de_followers:
            print("======== \n \n" + texte_du_tweet + "\n \nCe tweet fut envoyé par @" + user_name + "\n \n======== \n \n \n")
        else:
            pass

    def on_error(self, status_code):
        if status_code == 420:
            print(erreur_limite_atteinte)
        else:
            status_code = str(status_code)
            print ('Erreur ' + status_code)
            return True

    def on_timeout(self):
        print ('/!\ Connexion perdue /!\ ')
        return True

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['nox', 'noxhooves', 'noxshka'])
