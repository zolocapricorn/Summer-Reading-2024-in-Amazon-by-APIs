# Library Zone
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def requesting(url, head):
    """Requesting data from amazon website"""
    response = requests.get(url, headers=head)
    # return response
    if response:
        return BeautifulSoup(response.text, "lxml")

def book_name(soup):
    tags = soup.select_one("")
    return tags

def main():
    url = "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&ref=lp_122131175011_sar"
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept": "*/*", 
            "Referer": "https://www.amazon.com/"}
    soup = requesting(url, head)
    # print(soup)
    BookName = book_name(soup)
    # pprint(BookName)
    # data = soup.find("span", class_="a-truncate-full a-offscreen")
    # print(soup.find('div'))
    # print(data)
    
main()