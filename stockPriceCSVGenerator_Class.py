import time
from datetime import date
from csv import writer
from RedditWebCrawler_Class import RedditCrawler







class stockPriceGeneratorCSV:

    def __init__(self):
        pass


    # this function reads the stock list, and appends new row of data
    # to stock CSV file containing price and date of value
    def stockDataToCSV(self):

        redditCrawler = RedditCrawler() # this object is used to call the stock api
        # reads each of the stocks stored in stocklist
        with open('stockData/stockList.txt', 'r') as readFile:
            stockList = readFile.readlines()
            # print( '\n\n', stockList)
            readFile.close()

        
        for index,stock in enumerate(stockList):
            
            if stock != '\n' and stock != '':
                time.sleep(7.7) # Sleep for 7.7 seconds because API is limited to reading every 7 seconds
                price = redditCrawler.realTimePrice(stock.strip())
                # price = rerealTimePrice(stock.strip())
                # print(stock, price)
                if (price == -1):
                    pass
                else:
                    today = date.today()
                    stockDayValue = [stock.strip(), today, price]
                    with open(f'stockData/stockCSV/{stock.strip()}.csv', 'a', newline='') as csvDoc:  
                        writer_object = writer(csvDoc)
                        writer_object.writerow(stockDayValue)  
                        csvDoc.close()

        return


