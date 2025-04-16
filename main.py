import http.server
import requests
from bs4 import BeautifulSoup
import os
import subprocess


os.system('clear')
ip = str(input('Enter Your Target Ip Address: '))
port = int(input("Enter yout target port: "))

port = 8000
ip = "192.168.253.136"
url = f"http://{ip}:{port}"


def getDirectoryList(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')

    print("List of Directories : \n")
    for link in links:
        print(link.get('href'))
    if len(links) == 0:
        print("Empty Directory! Maybe this directory doesnt exists yet")


os.system('clear')
os.chdir('received/')

def menu():
    global url
    while(1):

        os.system('clear')
        print(f"Current Directory : {url}")
        getDirectoryList(url)
        print('''
            **
|          MENU            |
            **
| 1. Download a File       |
| 2. Go into A directory   |
| 3. Go back A directory   |
| 4. Exit                  |
            ** 
''')
        opt = input("\nWhat You Wanna do: ")

        if opt == '1':
            fileName = str(input("Which File To Download : "))
            dsuccess = True
            while dsuccess:
                try:
                    subprocess.run(["curl","-O", f"{url}/{fileName}"])
                    dsuccess = False
                except:
                    print("Error!File Not Found")
                    dsuccess = True
        elif opt == '2':
            fileName = str(input("Which Directory To Go : "))
            dsuccess = True
            while dsuccess:
                try:
                    url+=f"/{fileName}"
                    dsuccess = False
                except:
                    print("Error!File Not Found")
                    dsuccess = True
        elif opt == '3':
            url = url.rsplit('/',1)[0]
        elif opt == '4':
            print("Thanks for using me!")
            break
        # else:
        #     print("Invalid Option! Try Again")
menu()