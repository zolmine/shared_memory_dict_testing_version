from time import sleep
from source import shared

while True:
    try:
        loadedData = shared['data']
        for item in loadedData:
            print(item)
    except:
        print(False)
    sleep(5)