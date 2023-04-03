from urllib.request import urlopen
import json
import csv

URL = 'https://financialmodelingprep.com/api/v3/historical-price-full/GOOG?from=2011-10-06&to=2022-03-03&apikey=7721d4077165586091b074b581a88c16'
res = urlopen(URL)
data = res.read().decode('utf-8')
data = json.loads(data)
#print(data)
#print(data['historical'][1]['open'])
fields = ['date','open','close','high','low','volume']
with open('goog.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in range(len(data['historical'])):
        csvwriter.writerow([data['historical'][i]['date'],data['historical'][i]['open'],data['historical'][i]['close'],data['historical'][i]['high'],data['historical'][i]['low'],data['historical'][i]['volume']])