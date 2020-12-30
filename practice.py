import requests
from bs4 import BeautifulSoup

response = requests.get('https://spotifycharts.com/regional')
html = response.content
soup = BeautifulSoup(html, 'html.parser')
#print(soup)

list_song = soup.find_all(name="td", attrs={"class":"chart-table-track"})
list_artist = soup.find_all(name="td", attrs={"class":"chart-table-track"})

for index in range(len(list_song)):
    title = list_song[index].find('strong').text
    artist = list_artist[index].find('span').text
    print(index+1, " : ", title, ", by '{}'".format(artist))
    if index == 99:
        break