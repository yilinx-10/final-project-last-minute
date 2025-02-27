"""
Final Project: Reddit Scraping
Yilin Xu
"""
import praw
import numpy as np
import pandas as pd
import pprint
import json
import datetime
import prawcore
import time
import random

post_lst = []
comment_lst = []
pd.set_option('max_colwidth', None)

reddit = praw.Reddit(
    client_id="oCPIQsxeqy9ioFGkQNv26A",
    client_secret="07TikO3G7waJyTFTXACma2gsUnsPmg",
    password="macs30122",
    user_agent="Scraper for 122 Final Project by u/Background-Motor-921",
    username="Background-Motor-921"
)

start_date = '05-01-25 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

key_to_remove = ['_fetched', '_reddit', '_replies',\
                 '_submission', 'body_html', '_additional_fetch_params',\
                 '_comments', '_comments_by_id', 'selftext_html']

def clean_data(data, key_to_remove):
    data['author'] = data['author'].name if data['author'] else "Not Applicable"
    data['subreddit'] = data['subreddit'].display_name if data['subreddit'] else "Not Applicable"
    return {key: value for key, value in data.items() if key not in key_to_remove}

def process_comments(cf_lst):
    for comment in cf_lst:
        if isinstance(comment, praw.models.MoreComments):
            if comment.comments():
                process_comments(comment.comments())

        time.sleep(1)

        comment_data = clean_data(vars(comment), key_to_remove)
        comment_data.setdefault('title', '')
        comment_data['selftext'] = comment_data.get('body', '')

        # Calculate upvote ratio safely
        total_votes = comment_data.get('downs', 0) + comment_data.get('ups', 0)
        comment_data['upvote_ratio'] = (comment_data['ups'] / total_votes) if total_votes else 0.5

        # Count replies safely
        count = len(comment.replies)
        comment_data['num_crossposts'] = count
        comment_data['num_comments'] = count

        comment_lst.append(comment_data)

def safe_request():
    """Fetch posts while handling rate limits"""
    try:
        for post in reddit.subreddit("all").search("LA wildfire", sort="top", time_filter="month", limit= 250):  # Reduce limit
            date = post.created_utc
            if date < start_date:
                continue
            
            post_data = clean_data(vars(post), key_to_remove)
            post_lst.append(post_data)
            print("Processing Post:", post.title)

            post.comments.replace_more(limit=None)
            time.sleep(random.uniform(1, 3))

            if post.comments.list():
                process_comments(post.comments.list())
  
            time.sleep(random.uniform(1, 3))  # Respect Reddit's rate limit
    except prawcore.exceptions.TooManyRequests as e:
        print(f"Rate limit exceeded! ({e})")
    except:
        print(f"Error: ({e})")

safe_request()

with open('post_data_v3.json', 'w') as f:
    for obj in post_lst:
        f.write(json.dumps(obj) + "\n")

with open('comment_data_v3.json', 'w') as f:
    for obj in comment_lst:
        f.write(json.dumps(obj) + "\n")

print("Task Finished!")