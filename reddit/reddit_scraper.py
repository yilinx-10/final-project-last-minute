"""
Final Project: Reddit Scraping
Yilin Xu
"""
# Import packages
import praw
import numpy as np
import pandas as pd
import pprint
import json
import datetime
import prawcore
import time
import random

# Create Empty List to Store Information Scraped
post_lst = []
comment_lst = []
pd.set_option('max_colwidth', None)

# Load Authorized Reddit Instance
reddit = praw.Reddit(
    client_id="oCPIQsxeqy9ioFGkQNv26A",
    client_secret="07TikO3G7waJyTFTXACma2gsUnsPmg",
    password="macs30122",
    user_agent="Scraper for 122 Final Project by u/Background-Motor-921",
    username="Background-Motor-921"
)

# Set start date for contents to be scraped.
# Any posts posted before the start data will not be scraped
start_date = '05-01-25 00:00:00'
start_date = datetime.datetime.strptime(start_date, '%d-%m-%y %H:%M:%S').timestamp()

# Set a preliminary list of keys we wish to remove
# These keys are removed because they are problematic or unnecessary
key_to_remove = ['_fetched', '_reddit', '_replies',\
                 '_submission', 'body_html', '_additional_fetch_params',\
                 '_comments', '_comments_by_id', 'selftext_html']

def clean_data(data, key_to_remove):
    '''
    Keep data with needed keys and handle missing
    information on author and subreddit
    '''
    data['author'] = data['author'].name if data['author'] else "Not Applicable"
    data['subreddit'] = data['subreddit'].display_name if data['subreddit'] else "Not Applicable"
    return {key: value for key, value in data.items() if key not in key_to_remove}

def process_comments(cf_lst):
    '''
    Recursivelt process CommentForest(tree structure) and 
    MoreComments instances to obtain complete comments structure
    '''
    for comment in cf_lst:
        # check is the instance is MoreComment, if yes, need to expand
        if isinstance(comment, praw.models.MoreComments): 
            if comment.comments(): # expand MoreComments and check is not empty
                process_comments(comment.comments()) # recursion to extract the new CommentForest list

        time.sleep(1) # Respect Reddit's rate limit

        comment_data = clean_data(vars(comment), key_to_remove) # clean data, see helper function
        comment_data.setdefault('title', '') #set value for title in case there is None
        comment_data['selftext'] = comment_data.get('body', '') #save comment text value as selftext to align with post data key

        # Calculate upvote ratio safely
        total_votes = comment_data.get('downs', 0) + comment_data.get('ups', 0)
        comment_data['upvote_ratio'] = (comment_data['ups'] / total_votes) if total_votes else 0.5

        # Count replies safely
        count = len(comment.replies)
        comment_data['num_crossposts'] = count
        comment_data['num_comments'] = count

        # append to processed comment_lst
        comment_lst.append(comment_data)

def safe_request():
    '''
    Fetch posts while handling rate limits
    '''
    try:
        for post in reddit.subreddit("all").search("LA wildfire", sort="top", time_filter="month", limit= 250):  # Reduce limit
            date = post.created_utc
            # check if it posted later than indicated start date
            if date < start_date:
                continue
            
            # process post data with helper function
            post_data = clean_data(vars(post), key_to_remove)
            post_lst.append(post_data)
            print("Processing Post:", post.title) # Print statement: help keep track of progress

            # Extract all first level comments(directly replying to post) 
            post.comments.replace_more(limit=None)
            time.sleep(random.uniform(1, 3)) # Respect Reddit's rate limit

            if post.comments.list(): # if there are comments(CommentForest object), proceed to process them
                # Call recursive function on the list of CommentForest objects
                process_comments(post.comments.list())
  
            time.sleep(random.uniform(1, 3))  # Respect Reddit's rate limit
    except prawcore.exceptions.TooManyRequests as e:
        print(f"Rate limit exceeded! ({e})")
    except:
        print(f"Error: ({e})")

# Scrape!
safe_request()

# Save scraped posts
with open('reddit_post_data.json', 'w') as f:
    for obj in post_lst:
        f.write(json.dumps(obj) + "\n")

# Save scraped comments
with open('reddit_comment_data.json', 'w') as f:
    for obj in comment_lst:
        f.write(json.dumps(obj) + "\n")

# Notify
print("Task Finished!")

# Reflection 
# No AI is used to in any way for the codes in this file

# Reference
# PRAW documentation: https://praw.readthedocs.io/en/stable/getting_started/quick_start.html