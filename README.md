# Reddit-Mining-and-Stock-tracker

This program uses the Python package PRAW to connect with the Reddit API to web scrape subreddit post information 
on subreddits related to Stock Market discussion. It will web scrape a user defined amount of posts from the "top", "hot", and "new" categories 
for the definied subreddit. Upon collecting the title information from those categories, the posts will be analyzed to find  any time a specific
Stock name is mentioned. These stock names will be analyzed based on word frequency, and any frequently discussed about Stocks will be added to
a list of daily tracked stocks. The price of these Stocks will be checked daily and their daily prices will be logged in an individual CSV file
for each stock. Lastly the program will analyze all of the stock prices contained within the CSV, and it will notify the user via email of any 
significant changes in stock price over time.
