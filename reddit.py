import praw
import credentials

reddit = praw.Reddit(
    client_id = credentials.client_id,
    client_secret = credentials.client_secret,
    user_agent="my user agent",
)

for submission in reddit.subreddit("Eesti").new (limit=20):
    print(submission.title)
    print(submission.id)
    print(submission.score)
    print(submission.url)
    print(submission.author.name)
    print(submission.author.link_karma)
    submission.comment_sort = "new"
    top_level_comments = list(submission.comments)
    print(top_level_comments)