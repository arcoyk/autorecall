from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver_mac_85", options=options)
for animal in ["Dog", "Cat", "Bird", "Fish"]:
    driver.get("https://en.wikipedia.org/wiki/" + animal)
    print(driver.title)
driver.quit()
