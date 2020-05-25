#!/usr/bin/python
import praw
import pdb
import re
import os
import time

# Create the Reddit instance
reddit = praw.Reddit('hellothere')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("hellotherebot/posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("hellotherebot/posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


# Get the top 10 values from our subreddit
subreddit = reddit.subreddit('prequelmemes')
for submission in subreddit.new(limit=10):

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if (re.search("hello there", submission.title, re.IGNORECASE) or re.search("obi", submission.title, re.IGNORECASE) or re.search("obi-wan", submission.title, re.IGNORECASE) or re.search("kenobi", submission.title, re.IGNORECASE) or re.search("ewan", submission.title, re.IGNORECASE) or re.search("mcgregor", submission.title, re.IGNORECASE) or re.search("grievous", submission.title, re.IGNORECASE) or re.search("general", submission.title, re.IGNORECASE)) and not (re.search("chris",submission.title, re.IGNORECASE) or re.search("pratt",submission.title, re.IGNORECASE)):
            # Reply to the post
            submission.reply("hello there")

            # Store the current id into our list
            posts_replied_to.append(submission.id)

            # wait 1 seconds because reddit will only let you send a request 60 times per minute
            time.sleep(1)

            # upvote post
            submission.upvote()

            # wait 1 seconds because reddit will only let you send a request 60 times per minute
            time.sleep(1)

# previously saved all posts, but now we are only saving the most recent 10
# Write our updated list back to the file
# only write ten most recent items
with open("hellotherebot/posts_replied_to.txt", "w") as f:
    for i in xrange(-10,0): #post_id in posts_replied_to:
	f.write(posts_replied_to[i] + "\n")
#        f.write(post_id + "\n")
