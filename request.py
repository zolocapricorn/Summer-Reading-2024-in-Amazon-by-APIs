# Library Zone
import requests
# from bs4 import BeautifulSoup
from pprint import pprint

def requesting(url, head):
    """Requesting data from amazon website"""
    response = requests.get(url, headers=head)
    return response
    # if response:
    #     return bs4.BeautifulSoup(response.content, "lxml")

def book_name(soup):
    selector = 'span.a-size-medium.a-color-basea-text-normal'
    tags = soup.select_one(selector)
    return tags

def main():
    url = "https://www.amazon.com/s?rh=n%3A122131175011&fs=true&ref=lp_122131175011_sar"
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    soup = requesting(url, head)
    print(soup)
    # BookName = book_name(soup)
    # pprint(BookName)
    # data = soup.find("span", class_="a-truncate-full a-offscreen")
    # print(soup.find('div'))
    # print(data)
    
main()