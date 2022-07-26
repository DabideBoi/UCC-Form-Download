from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import json
from pathlib import Path

import glob
import os.path

def get_last_file():  
    folder_path = 'Files/'
    file_type = '/*txt'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    last_file = max_file.replace("Files\\", '')
    last_file = last_file.replace('.txt', '')
    return int(last_file)

def tag_visible(element):
    if element.parent.name in [
            'style', 'script', 'head', 'title', 'meta', '[document]'
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

#print(text_from_html(html) )

def initial_ping(latest = 8845):
    data = {}
    false_counter = 0
    for counter in range(latest, 15000):
        try:
            html = urllib.request.urlopen('https://ucc.ph/printformElemHigh/?StudentID=' + str(counter)).read()
            html = str(html)
            print("Counter: ", counter)
            if html.find("UNIDA CHRISTIAN COLLEGES") > 0:
                data[counter] = True
            else:
                false_counter = false_counter + 1
                if false_counter == 10:
                    break
        except:
            print("Error Occured")

    json_saver(data)

def parser(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')
        return data

def ping_parsed_checker():
    print("Hello")

def json_saver(dictionary):
    with open("ping.json", "w") as fp:
        json.dump(dictionary , fp) 

def json_open(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

def Find_keys_by_values(dict,val_to_find): 
   listofkeys = list()
   for key, value in dict.items(): 
      if value == val_to_find:
       listofkeys.append(key)
   print('key of given value\n =',listofkeys)

