from time import sleep
from source import shared

while True:
    try:
        loadedData = shared['data']
        print(loadedData)
    except:
        print(False)
    sleep(5)
