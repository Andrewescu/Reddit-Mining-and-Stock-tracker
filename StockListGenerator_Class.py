from RedditWebCrawler_Class import RedditCrawler
import string
import time
from collections import Counter

###
# this class will create/update a stock list
# this stock list will be composed of stocks discussed on specific subreddits
# in this case the "wallstreetbets" subreddit. It works taking as input webscraped reddit post titles,
# and finding names of stocks discussed therein. The names of stocks will be analyzed 
# by way of word frequency, and any stock being mentioned more than num times will be added
# to the stock list
###

class StockListGenerator:
    ### file path is used for read/writing of stockList
    def __init__(self, filePath, posts):
        self.filePath = filePath
        self.titleString = ''
        self.posts = posts
        self.wordFreqArr = []

    ### receives array of titles (posts) and concantenates all titles 
    ### into one big string, in order to parse and analyze word count
    ### each element in array has [post title, self text, and post id] - we're only using post title
    def prepareString(self):
        str = ''
        for post in self.posts:
            str = str +  ' ' + post[0] + ' '
        filter = string.punctuation + "0123456789"
        cleanStr = ''
        for char in str:
            if char not in filter:
                cleanStr = cleanStr + char
        self.titleString = cleanStr
        # print(self.titleString)
        return self.titleString


    ### takes a string of words, and firstly only uses words that are all caps
    ### this is to filter for potential stocks as generally they are written in all caps
    ### will return a 2-d array containing the words and their frequency
    ### uses self.titleString as string, must call prepare string first to populate titleString
    def wordFreqAllCaps(self):
        wordsFreq = []
        arr = Counter(self.titleString.split()).most_common() 
        for word, count in arr:
            if (word.isupper()):
                # print(word)
                wordsFreq.append([word,count])
        self.wordFreqArr = wordsFreq
        # print(wordsFreq)
        return wordsFreq


    ### will open file for writing at given filePath, and create it if it doesn't exist
    ### appends the provided string parameter to end of file
    def writeToTxt(self, str):
        # Open a file with access mode 'a'
        file_object = open(self.filePath, 'a')
        writeStr = '\n' + str 
        file_object.write(writeStr)
        # Close the file
        file_object.flush()
        file_object.close()
        


    ### will attempt to open file at given filePath
    ### for reading and will strip each line of surrounding whitespace
    def readTxt(self):
        try:
            readFile = open(self.filePath, 'r')
            
            str = readFile.readlines()
            
            readFile.close()
            for x in range(len(str)):
                str[x] = str[x].strip()
            return str
        except:
            return['']

    def theStockList(self, ocurrenceNum):
        redditCrawler = RedditCrawler()
        self.prepareString()
        self.wordFreqAllCaps()

        # print(self.wordFreqArr)
        print('Updating Stock List...')
        for entry in self.wordFreqArr:
            if (entry[1] >= ocurrenceNum): # if this specifc word is mentioned equal to or more than occurrenceNum times
                trackedStocks = self.readTxt()  # loads tracked stock list
                # whitelist = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') # this was used to filter out punctuation/numbers but this is handled elsewhere
                # filteredStr = ''.join(filter(whitelist.__contains__, entry[0]))
                if (entry[0] not in trackedStocks): # checks if specific stock is already in stockList
                    time.sleep(7.6)
                    assetPrice = redditCrawler.realTimePrice(entry[0])
                    if (assetPrice != -1): #if the word is a real stock, it adds it
                        self.writeToTxt(entry[0])

        return self.wordFreqArr


