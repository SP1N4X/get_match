#import datetime
#from datetime import datetime, timedelta
import requests

#next_match = '15:30'
#next_match = datetime.strptime(next_match, '%H:%M') - timedelta(minutes=1.5)
#print(next_match)
host = 'https://www.sisal.it'
url_alberatura = '/api-betting/vrol-api/vrol/palinsesto/getAlberaturaEventiSingoli/1'
headers = {"Referer": "https://www.betexplorer.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
s = requests.Session()
session = s.headers.update(headers)
request = s.get(host+url_alberatura)
response = request.status_code
print(response)
