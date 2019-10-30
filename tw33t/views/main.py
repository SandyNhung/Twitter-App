from flask import g, Markup
from flask import (Blueprint, render_template, make_response, 
redirect, url_for, abort, request, Response, session, jsonify)


from tw33t import app
from functools import wraps
from flask import jsonify
import json, requests, datetime, sys, os, uuid, re, time
import config
from tw33t.views.models import Person
import tweepy
import logging
import json

'''

Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''

people = []
api = None

auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def getTweet(name):

    #fetch user data
    try:
        user = api.get_user(name)
    except tweepy.error.TweepError:
        return {"Error": "Username is not Found"}

    #fetch timeline from input user name
    timeline = []
    try:
        timeline_from_api = tweepy.Cursor(api.user_timeline, screen_name="@" + name).items(3)

    except tweepy.error.TweepError:
        return{"Error": "Timeline is not found"}

    for status in timeline_from_api:
        timeline.append({
                "text": status.text,
                "created_at": status._json["created_at"],
                "retweet_count": status.retweet_count,
                "favorite_count": status.favorite_count,
                })
    #store data in people model
    person = Person(user.name, timeline, user.screen_name, user.profile_image_url)
    people.append(person)
    return person.__dict__

def getUser(name):
    
    try:
        users_list = api.search_users(q="@" + name, count=6)

    except:
        tweepy.error.TweepError

    if(len(users_list) == 0):
        return {"Error": "User not found!"}
    else:
        list = []
        for user in users_list:
            list.append({
                'screen_name': user._json['screen_name'],
                'name': user._json['name'],
                'profile_image': user._json['profile_image_url']
                })
        return list