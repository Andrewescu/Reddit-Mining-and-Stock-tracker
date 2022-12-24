import requests
import praw
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_AGENT = os.getenv('USER_AGENT')

# This class webscrapes a given subreddit, and 
# returns an array of the top num of posts in a given category
# the categories are "hot" "new" and "top"
# will be used to create stockList of stocks mentioned frequently on specific subreddits
# arrays contain [post.title, post.selftext, post.id]

class RedditCrawler:
    ### Stock API key is used for making call to stock api for stock prices
    ### client id, secrent, and user agent are used for webcrawling reddit with praw
    def __init__(self):
        self.STOCK_API_KEY = STOCK_API_KEY
        self.CLIENT_ID = CLIENT_ID
        self.CLIENT_SECRET = CLIENT_SECRET
        self.USER_AGENT = USER_AGENT
        

    ### makes an API call to the twelvedata API which is used for stock pricing
    ### sends a get request to the the twelve data api, the request includes the asset value which is the stock name and api key
    def realTimePrice(self, asset) :
        response = requests.get(f'https://api.twelvedata.com/price?symbol={asset}&apikey={STOCK_API_KEY}').json()
        try:
            status = response['status']
            if status == 'error':
                return -1
        except: 
            pass
        return response['price']


    ### access specific subreddit, returns array which is composed of strings of each title from num of posts in 'top' reddit category for the day
    def topPosts(self, subreddit, num):
        reddit = praw.Reddit(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, user_agent=self.USER_AGENT)
        posts = []
        theSubreddit = reddit.subreddit(subreddit)
        for post in theSubreddit.top(time_filter='day', limit=num):
            posts.append([post.title, post.selftext, post.id])
        return posts

    ### access specific subreddit, returns array which is composed of strings of each title from num of posts in 'new' reddit category for the day
    def newPosts(self, subreddit, num):
        reddit = praw.Reddit(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, user_agent=self.USER_AGENT)
        posts = []
        theSubreddit = reddit.subreddit(subreddit)
        for post in theSubreddit.new( limit=num):
            posts.append([post.title, post.selftext, post.id])
        return posts
 
    ### access specific subreddit, returns array which is composed of strings of each title from num of posts in 'hot' reddit category for the day
    def hotPosts(self, subreddit,num):
        reddit = praw.Reddit(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET, user_agent=self.USER_AGENT)
        posts = []
        theSubreddit = reddit.subreddit(subreddit)
        for post in theSubreddit.hot(limit=num):
            posts.append([post.title, post.selftext, post.id])
        return posts



