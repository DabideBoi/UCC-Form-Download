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

def main():
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
        
        #download_text(variable)
        pinger.initial_ping()
        file = pinger.json_open("ping.json")
        last = int(list(file.keys())[-1])
        print(last)
        webscraper.download_text(last)
        prsr.data_to_csv(last)

       
        
    else:
        print("false")
        pinger.initial_ping()
        file = pinger.json_open("ping.json")
        last = int(list(file.keys())[-1])
        webscraper.download_text(last)
        prsr.data_to_csv(last)

if __name__=="__main__":
    main()