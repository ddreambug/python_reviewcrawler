from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

#url masukin sini
url = "https://www.tokopedia.com/allforgadget/premium-silicone-matte-case-iphone-12-case-iphone-12-pro-max-12-mini-hitam-ip-12-mini/review"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)

data = []
for i in range(0, 10):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    containers = soup.findAll('article', attrs = {'class':'css-72zbc4'})

    for container in containers:
        try:

            a = container.find('span', attrs = {'class':'name'}).text
            b = container.find('p', attrs = {'data-testid':"lblVarian"}).text
            c = container.find('span', attrs = {'data-testid':'lblItemUlasan'}).text

            data.append(
                (a,b,c)
            )
        except AttributeError:
            continue

    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']").click()
    time.sleep(3)

print(data)

df = pd.DataFrame(data, columns=['nama','barang','ulasan'])
df.to_csv("Tokopedia.csv", index=False)