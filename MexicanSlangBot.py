import praw

r = praw.Reddit('Mexican Slang Bot 1.0 by u/CockMySock')
r.login('MexicanSlangBot', 'bucalesa')
prawWords = ['I am going to kill you.', 'I\'m gonna kill you.', 'I\'ll kill you.', 'I will kill you', 'I will hurt you', 'I\'m gonna hurt you.', 'I am going to hurt you.', 'I\'ll hurt you.']
already_done = []
while True:
    subreddit = r.get_subreddit('cocktest')
    subreddit_comments = subreddit.get_comments()
    for comment in subreddit_comments:
        if comment.id not in already_done:
            has_praw = any(string in comment.body for string in prawWords)
            if comment.body and has_praw:
                #comment.reply('I\'ll cut you, ese.')
                already_done.append(comment.id)