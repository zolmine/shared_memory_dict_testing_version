from time import sleep
from source import shared

while True:
    try:
        loadedData = shared['data']
    except:
        loadedData = []
    data = {'me1':34, 'me2':56, 'me3':78}
    loadedData.append(data)
    shared['data'] = loadedData
    sleep(3)