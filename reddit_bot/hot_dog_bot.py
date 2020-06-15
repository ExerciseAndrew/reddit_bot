import praw


reddit = praw.Reddit('bot1', user_agent='bot2 user agent') # you can obviate passing user_agent if you add the setting user_agent=... in the [bot2] site definition.