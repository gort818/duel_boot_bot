import praw
import config
import re
import os

		

reddit=praw.Reddit(client_id=' ',
		client_secret=' ',
		user_agent = ' ',
        username=' ',
        password=' ')

print(reddit.read_only) # if false you have write access if true you have only read access

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Get values from our subreddit
subreddit = reddit.subreddit('enter subreddit here')


for submission in subreddit.new():

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

       # Do a case insensitive search
        duel = re.search("duel", submission.title, re.IGNORECASE)
        if duel:
            # Reply to the post
            bot_reply=("""What I think you mean is Dual boot. \n\nDual Booting is the act of installing multiple operating systems on a computer, and being able to choose which one to boot. Duel boot is a boot(shoewear) used in dueling(arranged combat).\n\n ***\n ^[ ^Just ^another ^bot. [^Source](https://github.com/gort818/duel_boot_bot) ^]""")


            submission.reply(bot_reply)
            print("Found in ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)
# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

