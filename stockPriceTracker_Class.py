import os
import csv
import datetime




class stockPriceTracker:
    def __init__(self):
        os.chdir('stockData/stockCSV')
        self.files  = os.listdir()
        self.changeList = []
        

    def stockTracker(self, fileName):
        stockName = fileName[:-4]
        rowArr = []
        with open(fileName, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row != []:
                    rowArr.append(row)

        lastIndex = len(rowArr)-1

        # if CSV has atleast 2 days of values
        if len(rowArr) > 1:
            #price difference between today and yesterday
            yesterdayVal = float(rowArr[lastIndex-1][2])
            todayVal = float(rowArr[lastIndex][2])
            dayDifference =   todayVal - yesterdayVal

            if dayDifference > 0: # value grew
                percentChange = dayDifference/yesterdayVal
                percentChange = percentChange * 100
                if abs(percentChange) > 3.0:
                    print("########################## ", f'{percentChange}')
                    self.changeList.append(f'{stockName} daily percent change:' + " " + f'{percentChange:+.4}' + "%")
                    print(f'{stockName} daily percent change:',f'{percentChange:+.4}' + "%")

            elif dayDifference == 0:
                print(f'{stockName} no daily change')

            elif dayDifference < 0: # value shrank
                percentChange = dayDifference/yesterdayVal
                percentChange = percentChange * 100
                if abs(percentChange) > 3.0:
                    print("########################## ", f'{percentChange}')
                    self.changeList.append(f'{stockName} dailly percent change:' + " " + f'{percentChange:+.4}' + "%")
                    print(f'{stockName} dailly percent change:' + " " + f'{percentChange:+.4}' + "%")

        # if CSV has atleast a week of values
        if len(rowArr) > 6:
            weekAgoVal = float(rowArr[lastIndex-6][2])
            todayVal = float(rowArr[lastIndex][2])
            weekDifference = todayVal - weekAgoVal
            # print("week diff: ", f'{weekDifference:+.6}')

            if weekDifference > 0: #value grew
                percentChange = weekDifference/weekAgoVal
                percentChange = percentChange * 100
                if abs(percentChange) > 6.0:
                    self.changeList.append(f'{stockName} weekly percent change:'+ " " + f'{percentChange:+.4}' + "%")
                    print(f'{stockName} weekly percent change:',f'{percentChange:+.4}' + "%")

            elif weekDifference == 0:
                print(f'{stockName} no weekly change')

            elif weekDifference < 0: # value shrank
                percentChange = weekDifference/weekAgoVal
                percentChange = percentChange * 100
                if abs(percentChange) > 6.0:
                    self.changeList.append(f'{stockName} weekly percent change:' + " " + f'{percentChange:+.4}' + "%")
                    print(f'{stockName} weekly percent change:',f'{percentChange:+.4}' + "%")

        # if CSV has atleast a month (4 weeks) of values
        if len(rowArr) > 27:
            monthAgoVal = float(rowArr[lastIndex-27][2])
            todayVal = float(rowArr[lastIndex][2])
            monthDifference =todayVal - monthAgoVal
 
            if monthDifference > 0: # value grew
                percentChange = monthDifference/monthAgoVal
                percentChange = percentChange * 100
                if abs(percentChange) > 11.0:
                    self.changeList.append(f'{stockName} monthly percent change:' + " " + f'{percentChange:+.4}' + "%")
                    print(f'{stockName} monthly percent change:',f'{percentChange:+.4}' + "%")

            elif monthDifference == 0:
                print(f'{stockName} no monthly change')

            elif monthDifference < 0: # value shrank
                percentChange = monthDifference/monthAgoVal
                percentChange = percentChange * 100
                if abs(percentChange) > 11.0:
                    self.changeList.append(f'{stockName} monthly percent change:' + " " + f'{percentChange:+.4}' + "%")
                    print(f'{stockName} monthly percent change:',f'{percentChange:+.4}' + "%")

            

    def runStockTracker(self):
        # print(self.files)

        with open("/home/andrewescu/code/stock_webScraper_tracker/stockData/stockChanges/theUpdate.txt", 'w') as file:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            file.write(today + '\n')

        for fileName in self.files:
            self.stockTracker(fileName)

        with open("/home/andrewescu/code/stock_webScraper_tracker/stockData/stockChanges/theUpdate.txt", 'a') as file:
                for line in self.changeList:
                    file.write(line + '\n')
        
  

theTracker = stockPriceTracker()

theTracker.runStockTracker()