#!/usr/bin/python
import praw
import pdb
import re
import os
import time

# Create the Reddit instance
reddit = praw.Reddit('acnhturnips')

# Have we run this code before? If not, create an empty list
if not os.path.isfile("logs/acnhturnips/posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("logs/acnhturnips/posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))


# Get the top 10 values from our subreddit
subreddit = reddit.subreddit('acnhturnips')
for submission in subreddit.new(limit=10):

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search('nook', submission.title, re.IGNORECASE):
            num = 0
            mult = 1
            for i in reversed(submission.title):
                if i.encode('utf-8') == '0' or i.encode('utf-8') == '1' or i.encode('utf-8') == '2' or i.encode('utf-8') == '3' or i.encode('utf-8') == '4' or i.encode('utf-8') == '5' or i.encode('utf-8') == '6' or i.encode('utf-8') == '7' or i.encode('utf-8') == '8' or i.encode('utf-8') == '9':
                    num += int(i.encode('utf-8')) * mult
                    mult = mult * 10

            if num > 499:
                print submission.title.encode('utf-8').strip()
                print num

                # Reply to the post
                submission.reply("I am interested! Can I please get your dodo code?");

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
with open("logs/acnhturnips/posts_replied_to.txt", "w") as f:
    for i in xrange(-10,0): #post_id in posts_replied_to:
	f.write(posts_replied_to[i] + "\n")
#        f.write(post_id + "\n")
