from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.get('https://oscar.go.com/winners')
driver.implicitly_wait(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
category = soup.select('bls-winners-list > ul > li > div.winners-list__info > a')
movie = soup.select('bls-winners-list > ul > li > div.winners-list__info > h3 > a')
producer = soup.select('bls-winners-list > ul > li > div.winners-list__info > p')
oscars_2020 = []
for item in zip(category, movie, producer):
    oscars_2020.append(
        {
            'category': item[0].text,
            'movie': item[1].text,
            'producer': item[2].text
        }
    )
print(oscars_2020)
driver.quit()
