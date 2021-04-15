from bs4 import BeautifulSoup
import requests
import urllib.request
import re


def scarping_img_html(url,image_type,Folder_path):
    html_page = requests.get(url)

    soup = BeautifulSoup(html_page.content, 'html.parser')

    x = {""}
    for item in soup.find_all('img'):
        try:
            x.add(item['src'])
        except :
            print(TypeError)

    for i in x:
        result = re.search('List_(.*)'+'.'+image_type, i)
        if result is not None:
            urllib.request.urlretrieve(i, Folder_path + '/' + result.group(1) +'.'+image_type)
            print(result.group(1))
