#!/usr/bin/env python
import boto3
# import configparser
import feedparser
import json
import os
import requests
from slackclient import SlackClient

def get_entry_id(feed):
    '''
        feed: feedparser object
        gets entry id time of feed, throws it into a statefile for analysis
    '''
    return feed.entries[0].id

def write_entry_id(feed):
    """
    Writes entry id to a file. Temp for now, will be replaced by cloudy things later
    """
    with open('entry_id', 'w') as content_file:
        file_entry_id = content_file.write(get_entry_id(feed))

def compare_entry_id(feed):
    """
    Compares the pre-existing entry_id vs the new one 
    TODO: Refactor once we do cloudy things
    """
    with open('entry_id', 'r') as content_file:
        file_entry_id = content_file.read()
    print(file_entry_id)
    entry_id = get_entry_id(feed)
    print(entry_id)

    if file_entry_id in entry_id:
        print("nothing new to see here")
    else:
        print("new things")
        write_entry_id(feed)

url = "https://status.cloud.google.com/feed.atom"
feed = feedparser.parse (url)
foo = compare_entry_id(feed)
