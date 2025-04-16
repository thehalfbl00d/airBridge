import http.server
import requests
from bs4 import BeautifulSoup
import os

port = 8000
ip = '192.168.253.136'
url = f"http://{ip}:{port}/"


def getDirectoryList(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    os.system('clear')

    print("list of directories : \n")
    for link in links:
        print(link.get('href'))

getDirectoryList(url)

def changeDirectory(url, file, direction):
    url+=f"/{file}"

