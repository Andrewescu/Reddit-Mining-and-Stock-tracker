import os
import csv





class stockPriceTracker:
    def __init__(self):
        os.chdir('stockData/stockCSV')
        self.files  = os.listdir()
        

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

            if dayDifference > 0:
                percentChange = dayDifference/yesterdayVal
                print(f'{stockName} daily percent change:',f'{percentChange:+.2%}')

            elif dayDifference == 0:
                print(f'{stockName} no daily change')

            elif dayDifference < 0:
                percentChange = dayDifference/yesterdayVal
                print(f'{stockName} dailly percent change:',f'{percentChange:+.2%}')

        # if CSV has atleast a week of values
        if len(rowArr) > 6:
            weekAgoVal = float(rowArr[lastIndex-6][2])
            todayVal = float(rowArr[lastIndex][2])
            weekDifference = todayVal - weekAgoVal
            # print("week diff: ", f'{weekDifference:+.2}')

            if weekDifference > 0:
                percentChange = weekDifference/weekAgoVal
                print(f'{stockName} weekly percent change:',f'{percentChange:+.2%}')

            elif weekDifference == 0:
                print(f'{stockName} no weekly change')

            elif weekDifference < 0:
                percentChange = weekDifference/weekAgoVal
                print(f'{stockName} weekly percent change:',f'{percentChange:+.2%}')

        # if CSV has atleast a month (4 weeks) of values
        if len(rowArr) > 27:
            monthAgoVal = float(rowArr[lastIndex-27][2])
            todayVal = float(rowArr[lastIndex][2])
            monthDifference =todayVal - monthAgoVal

            if monthDifference > 0:
                percentChange = monthDifference/monthAgoVal
                print(f'{stockName} monthly percent change:',f'{percentChange:+.2%}')

            elif monthDifference == 0:
                print(f'{stockName} no monthly change')

            elif monthDifference < 0:
                percentChange = monthDifference/monthAgoVal
                print(f'{stockName} monthly percent change:',f'{percentChange:+.2%}')

    def runStockTracker(self):
        # print(self.files)
        for fileName in self.files:
            self.stockTracker(fileName)
  

