import praw

r = praw.Reddit('Mexican Slang Bot 1.0 by u/ComSock')
r.login('MexicanSlangBot', '')
prawWords = ['Hola.']
already_done = []
while True:
    subreddit = r.get_subreddit('comtest')
    subreddit_comments = subreddit.get_comments()
    for comment in subreddit_comments:
        if comment.id not in already_done:
            has_praw = any(string in comment.body for string in prawWords)
            if comment.body and has_praw:
                #comment.reply('I\'ll cut you, ese.')
                already_done.append(comment.id)
