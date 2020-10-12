from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
for animal in ["Dog", "Cat", "Bird", "Fish"]:
    driver.get("https://en.wikipedia.org/wiki/" + animal)
    print(driver.title)
driver.quit()
