import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = ("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C"
       "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122"
       ".30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22"
       "%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D"
       "%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value"
       "%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22"
       "%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C"
       "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C"
       "%22mapZoom%22%3A12%7D")

FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLSd5Ie7WDxpMIAV1KE8-u6u2avw-dfsdpkRLm-8N2ErNsA4acQ/viewform"
HEADERS = {
    "REQUEST-LINE": "GET / HTTP/1.1",
    "Accept-Language": "en-US,en;q=0.5",
    "ACCEPT-ENCODING": "gzip, deflate, br",
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "SEC-FETCH-DEST": "document",
    "SEC-FETCH-MODE": "navigate",
    "SEC-FETCH-SITE": "cross-site",
    "SEC-FETCH-USER": "?1",
    "SEC-GPC": "1",
    "TE": "trailers",
    "UPGRADE-INSECURE-REQUESTS": "1",
    "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
}

# getting the link, address, and price
request = requests.get(url=URL, headers=HEADERS).text
soup = BeautifulSoup(request, "lxml")
all_prices = [x.get_text().strip("$/mobd+ ").split("+")[0] for x in
              soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 "
                                                "iMKTKr")]
all_locations = [x.get_text() for x in soup.find_all("address")]
all_links = [x.get('href') for x in soup.find_all("a", class_="jnnxAW")]


# making a dictionary from the collected information
dicti = {}
for i in range(len(all_prices)):
    dicti.update({i: {0: all_locations[i],
                      1: all_prices[i],
                      2: all_links[i]}
                  }
                 )

# submitting info through Google forms
firefox_options = webdriver.FirefoxOptions().set_preference("detach", True)
driver = webdriver.Firefox(firefox_options)
for item in range(len(all_prices)):
    driver.get(FORMS_URL)
    time.sleep(5)
    all_fields = driver.find_elements(By.CLASS_NAME, "zHQkBf")
    submit = driver.find_element(By.CLASS_NAME, "NPEfkd")
    for i in range(len(all_fields)):
        all_fields[i].send_keys(dicti[item][i])
    submit.click()
    time.sleep(5)

driver.close()
driver.quit()



