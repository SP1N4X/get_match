import requests
import time
from datetime import datetime, timedelta
import json

host = 'https://www.sisal.it'
url_alberatura = '/api-betting/vrol-api/vrol/palinsesto/getAlberaturaEventiSingoli/1'
url_eventoSingolo =	'/api-betting/vrol-api/vrol/palinsesto/getDettaglioEventiSingoli/1/'
url_result = '/api-betting/vrol-api/vrol/archivio/getArchivioGareEventiSingoli/1/31/5/'

headers = {"Referer": "https://www.betexplorer.com",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
s = requests.Session()
session = s.headers.update(headers)

file = 'json.json'

def addResult(new): # FINITO #
    global file
    a_file = open(file, "r")
    json1 = json.load(a_file)
    json1[-2].update(new)
    a_file.close()

    b_file = open(file, "w")
    json.dump(json1, b_file)
    b_file.close()

def addMatch(new): # FINITO #
    global file
    a_file = open(file, "r")
    json1 = json.load(a_file)
    json1.append(new)
    a_file.close()

    b_file = open(file, "w")
    json.dump(json1, b_file)
    b_file.close()

def getEvento(): # FINITO #
    request = s.get(host+url_alberatura)
    response = request.json()
    for index in response:
        if index['descrdisc'] == 'Football':
            dati_1 = index['sogeicodpalinsesto']
            dati_2 = index['sogeicodevento']
            return dati_1, dati_2  
    
def getOdds(): # FINITO #
    global next_match
    palinsesto = getEvento()[0]
    evento = getEvento()[1]
    url_evento = host + url_eventoSingolo + '/' + palinsesto + '/' + evento
    request = s.get(url_evento)
    response = request.json()
    squadra_casa = response[0]['playerVirtualeList'][0]['name']
    squadra_ospite = response[0]['playerVirtualeList'][1]['name']
    orario = response[0]['formattedOrario']
    new = {'casa': squadra_casa, 'ospite': squadra_ospite, 'orario': orario}
    for baseList in response[0]['scommessaVirtualeBaseList']:
        for esitoList in baseList['esitoVirtualeList']:
            desc = esitoList['descrizione']
            quota = esitoList['quota']/100
            a = {desc:quota}
            new.update(a)
    addMatch(new)
    next_match = response[1]['formattedOrario']
    next_match = datetime.strptime(next_match, '%H:%M') - timedelta(minutes=1)
    next_match = next_match.strftime('%H:%M')
    getResult()
    

def getResult(): # FINITO # 
    data = datetime.now().strftime("%d-%m-%Y")
    url = host + url_result + data
    request = s.get(url)
    index = request.json()[-1]
    for lista in index['risultatoScommessaUfficialeList']:
        if lista['descrizioneScommessa'] == 'Risultato Esatto':
            esito = lista['descrizioneEsito']
            new = {'Risultato': esito}
            addResult(new)

def getNextMatch(): # FINITO #
    global next_match
    palinsesto = getEvento()[0]
    evento = getEvento()[1]
    url_evento = host + url_eventoSingolo + '/' + palinsesto + '/' + evento
    request = s.get(url_evento)
    response = request.json()
    next_match = response[1]['formattedOrario']

def run():
            data = datetime.now()
            getNextMatch()
            next_match = datetime.strptime(next_match, '%H:%M') - timedelta(minutes=1)
            next_match = next_match.strftime('%H:%M')
            a = True
            while a == True:
                        now = datetime.now()
                        timer = now.strftime("%H:%M")
                        if timer==next_match:
                                    print('in esecuzione')
                                    getOdds()
                                    print('FATTO!')
                        else:
                                    print(timer)
                                    print(next_match)
                                    time.sleep(20)
                                    print('-')

