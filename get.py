#import datetime
#from datetime import datetime, timedelta
import requests

try:
    #next_match = '15:30'
    #next_match = datetime.strptime(next_match, '%H:%M') - timedelta(minutes=1.5)
    #print(next_match)
    host = 'https://www.sisal.it'
    url_alberatura = '/api-betting/vrol-api/vrol/palinsesto/getAlberaturaEventiSingoli/1'
    headers = {'User-Agent':'Mozilla/5.0'}
    s = requests.Session()
    session = s.headers.update(headers)
    request = s.get(host+url_alberatura)
    response = request.status_code
    print(response)
except Exception as e:
    print(e)
