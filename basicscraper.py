"""
Created on Sat Aug  4 16:53:30 2018
Basic Web Scraper
@author: Brad
"""
import requests
from bs4 import BeautifulSoup 
try:
        import requests
        from bs4 import BeautifulSoup
except:
        print("Please import requests and BeautifulSoup and try again.")
    
def basicscraper():
        """Basic scraper that takes user input for url, HTML tag and output text file name.
    
        url              --user input for the target url
        new_scrape_name  --user input for output text file
        what             --user input for HTML tag    
        """
    
        url = str(input("Enter url: "))
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"lxml")
        new_scrape_name = str(input("Enter text file name: "))
        output = open(new_scrape_name + ".txt", "a")
        what = str(input("What HTML tag are you looking for? (h3,a,p, etc.) : "))
        for something in soup.find_all(what):
            a = something.text.strip()
            output.write("\n" + a + "\n")
        output.close

basicscraper()

