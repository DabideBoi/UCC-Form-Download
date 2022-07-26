from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import os
import json
from pathlib import Path
import csv
import converter as prsr
import pinger
import webscraper
import cleaner

import time



def main():
    while True:
        path_to_file = 'ping.json'
        path = Path(path_to_file)   
        if path.is_file():
            """print("true")
            data = pinger.json_open("ping.json")
            unloaded = [k for k,v in data.items() if v == False]
            print(unloaded)
            for counter in unloaded:
                try:
                    html = urllib.request.urlopen('https://ucc.ph/printformElemHigh/?StudentID=' + str(counter)).read()
                    html = str(html)
                    print("Counter: ", counter)
                    if html.find("UNIDA CHRISTIAN COLLEGES") > 0:
                        data[counter] = True
                    else:
                        data[counter] = False
                except:
                    print("Error Occured")

            with open('ping1.txt', 'w', encoding='utf-8') as f:
                    f.write(str(data))
                    f.close()"""
            print("false")
            file = pinger.json_open("ping.json")
            last = int(list(file.keys())[-1]) #last pinged active
            latest = pinger.get_last_file() #latest file downloaded
            print("last file:", latest)
            pinger.initial_ping(latest)
            print("Downloading...")
            webscraper.download_text(last, latest)
            print("Downloading Complete")
            print("Parsing to CSV")
            prsr.data_to_csv(last, latest)
            print("Parsing Complete")
            print("Checking Duplicates")
            cleaner.clean()
            print("File is all set")
            
        else:
            #download_text(variable)
            pinger.initial_ping()
            file = pinger.json_open("ping.json")
            last = int(list(file.keys())[-1])
            print(last)
            webscraper.download_text(last)
            prsr.data_to_csv(last,latest)
            print("Checking Duplicates")
            cleaner.clean()
            print("File is all set")
        time.sleep(30)

if __name__ == '__main__':
    main()