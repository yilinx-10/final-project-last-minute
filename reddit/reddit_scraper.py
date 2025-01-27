"""
Final Project: Reddit Scraping
Yilin Xu
"""
import praw
import numpy as np
import pandas as pd
import pprint
import json
import time

post_lst = []
comment_lst = []
pd.set_option('max_colwidth', None)

reddit = praw.Reddit(
    client_id="i_v3iJUCn5hWxYjgomFomw",
    client_secret="gPdZVrgfpB5gpGSD-jYFOMEMfjjCXA",
    password="macs30122",
    user_agent="Scraper122",
    username="enailenaile",
)

key_to_remove = ['_fetched', '_reddit',  '_replies',\
                 '_submission', 'body_html', '_additional_fetch_params',\
                 '_comments', '_comments_by_id', 'selftext_html']

def clean_data(data, key_to_remove):
    data['author'] = data['author'].name if data['author'] else "Not Applicable"
    data['subreddit'] = data['subreddit'].display_name if data['subreddit'] else "Not Applicable"
    return {key: value for key, value in data.items() if key not in key_to_remove}

for post in reddit.subreddit("All").search("LA wildfire", "new", "day"):
    post_data = clean_data(vars(post), key_to_remove)
    post_lst.append(post_data)
    post.comments.replace_more(limit=None)
    if post.comments.list() != []:
        for comment in post.comments.list():
            comment_data = clean_data(vars(comment), key_to_remove)
            comment_data.setdefault('title', '')
            comment_data['selftext'] = comment_data['body']
            sum = comment_data['downs'] + comment_data['ups']
            if sum != 0:
                comment_data['upvote_ratio'] = comment_data['ups'] / sum
            else:
                comment_data['upvote_ratio'] = 0.5
            count = comment.replies.__len__()
            comment_data['num_crossposts'] = count
            comment_data['num_comments'] = count
            comment_lst.append(comment_data)
    #time.sleep(2)

with open('post_data.json', 'w') as f:
    for obj in post_lst:
        f.write(json.dumps(obj) + "\n")

with open('comment_data.json', 'w') as f:
    for obj in comment_lst:
        f.write(json.dumps(obj) + "\n")

print("Task Finished!")

# # assume you have a praw.Reddit instance bound to variable `reddit`
# submission = reddit.submission("1ib8blh")
# print(submission.title)  # to make it non-lazy
# pprint.pprint(vars(submission))


# # assume you have a praw.Reddit instance bound to variable `reddit`
# comment = reddit.comment("m9fr423")
# print(comment.body)  # to make it non-lazy
# pprint.pprint(vars(comment))

