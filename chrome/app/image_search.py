from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

class ImageSearch:
    def by_tag(self, tag):
        return self.driver.find_elements_by_tag_name(tag)
    
    def atb(self, webelement, a):
        return webelement.get_attribute(a)
    
    def by_tag_atb(self, t, ak, av):
        return list(filter(lambda x: self.atb(x, ak) == av, self.by_tag(t)))
    
    def get_imgs(self):
        elems = self.by_tag("img")
        atbs = ["width", "height", "src", "alt"]
        items = []
        for elem in elems:
            item = {atb: elem.get_attribute(atb) for atb in atbs}
            items.append(item)
        return items
    
    def goodones(self, items):
        return list(filter(lambda x: int(x["width"]) > 100, items))
        
    def quit(self):
        self.driver.quit()
        
    def home(self):
        self.driver.get("https://www.google.com/search?q=cat&tbm=isch")
    
    def search(self, q):
        q = str(q)
        search_box = self.by_tag_atb("input", "title", "Search")[0]
        search_box.clear()
        search_box.send_keys(q + "\n")
        items = self.get_imgs()
        items = self.goodones(items)
        return items[:10]
            
    def __init__(self, driver, headless=False):
        self.options = Options()
        if headless:
            self.options.add_argument("--headless")
            self.options.add_argument("--no-sandbox")
            self.options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(driver, options=self.options)
        self.home()
