# Library Zone
import requests
from bs4 import BeautifulSoup
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
    # url = "http://books.toscrape.com/catalogue/page-1.html"
    url = "https://www.amazon.com/b/?_encoding=UTF8&node=122131175011&ref_=s9_acsd_al_ot_c2_x_clnk&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-6&pf_rd_r=1THR539952B75Y0C79BJ&pf_rd_p=cc704197-820b-47e2-bd80-1ab435ffa774&pf_rd_t=&pf_rd_i=23901427011"
    # "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&qid=1723994262&ref=sr_pg_1"
    # "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&page=2&qid=1723994419&ref=sr_pg_2"
    # "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&page=1qid=1723994427&ref=sr_pg_1"
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    soup = requesting(url, head)
    print(soup)
    # BookName = book_name(soup)
    # pprint(BookName)
    # data = soup.find("span", class_="a-truncate-full a-offscreen")
    # print(soup.find('div'))
    # print(data)
    
main()