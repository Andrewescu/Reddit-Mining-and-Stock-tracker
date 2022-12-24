from RedditWebCrawler_Class import RedditCrawler
from StockListGenerator_Class import StockListGenerator
from stockPriceCSVGenerator_Class import stockPriceGeneratorCSV
from stockPriceTracker_Class import stockPriceTracker
from datetime import datetime
import os

### calls an instance of all 4 classes to webscrape, load, and track stocks over time that
### are mentioned in a specific subreddit, in this case the 'wallstreetbets' subreddit
def run():

    ### This section of code, calls the web crawler which
    ### webscrapes reddit posts for a specific subreddit postToCrawl num of times
    ### and adds thats that appear wordFreqAmount or more times to stock list
    postsToCrawl = 100
    wordFreqAmount = 3

    redditCrawler = RedditCrawler()
    topPosts = redditCrawler.topPosts('wallstreetbets', postsToCrawl)
    hotPosts = redditCrawler.hotPosts('wallstreetbets', postsToCrawl)
    newPosts = redditCrawler.newPosts('wallstreetbets', postsToCrawl)

    top_posts_stock_list = StockListGenerator("stockData/stockList.txt", topPosts)
    top_posts_stock_list.theStockList(wordFreqAmount)

    hot_posts_stock_list = StockListGenerator("stockData/stockList.txt", hotPosts)
    hot_posts_stock_list.theStockList(wordFreqAmount)

    new_posts_stock_list = StockListGenerator("stockData/stockList.txt", newPosts)
    new_posts_stock_list.theStockList(wordFreqAmount)

    ### This code generates or appends a stock it's own CSV, which lists the date and value of the stock
    makerCSV = stockPriceGeneratorCSV()
    makerCSV.stockDataToCSV()

    ### This code runs the tracker, which reports percent changes in stock over time
    tracker = stockPriceTracker()
    tracker.runStockTracker()   



if __name__ == "__main__":
        
    ### this block of code checks if program has already been fun today
    ### and if it has, it doesn't run again

    today = datetime.today().strftime("%Y-%m-%d")
    
    # Check if the file exists
    if not os.path.exists("lastRan.txt"):
        # If the file doesn't exist, create it
        open("lastRan.txt", "w").close()

    # Open the file in read mode
    with open("lastRan.txt", "r") as f:
        # Read the first line of the file into a variable
        theLastDate = f.readline()
        if theLastDate != str(today):
            print("Running Stock Tracker")
            with open("lastRan.txt", "w") as file:
                    # Write the date to the file
                    file.write(str(today))

            try:
                run()
                

            except Exception as e:
                with open("error.txt", "w") as f:
                    f.write(str(e))
        else:
            print(f'Stock tracker already ran {today}')
