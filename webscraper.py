from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request
import os
from pathlib import Path


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u"\n".join(t.strip() for t in visible_texts)

def download_text(latest_form_active):
    for control_number in range(8845, latest_form_active):
        path = 'Files/' + str(control_number) + '.txt'
        path = Path(path)   
        if path.is_file():
            continue
        else:
            print("saving " + 'Files/' + str(control_number) + '.txt')
            html = urllib.request.urlopen('https://ucc.ph/printformElemHigh/?StudentID=' + str(control_number)).read()
            #print(text_from_html(html))
            file = text_from_html(html)
            text = "\n".join([ll.rstrip() for ll in file.splitlines() if ll.strip()])
            os.system('cls')
            print("Printing Number: " + str(control_number))
            with open('Files/' + str(control_number) + '.txt', 'w', encoding='utf-8') as f:
                f.write(text)

