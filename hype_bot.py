#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("paragon")

for submission in subreddit.new(limit=20):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
