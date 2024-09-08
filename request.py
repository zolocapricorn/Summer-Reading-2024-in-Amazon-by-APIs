# Library Zone
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def requesting(url, head):
    """Requesting data from amazon website"""
    response = requests.get(url, headers=head)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "lxml")
    return "Cannot requesting"


def book_name(soup):
    tags = soup.select("span.a-size-medium")
    book_list = [book.text for book in tags]
    return book_list


def writer_seller_kindle(soup):
    tags = soup.select("a.a-size-base")
    writer_seller_kindle_list = [writer.text for writer in tags]
    writer_list, seller_list, kindle_list = [], [], []
    for count in range(len(writer_seller_kindle_list)):
        if count%3 == 0:
            writer_list.append(writer_seller_kindle_list[count])
        elif count%3 == 1:
            seller_list.append(writer_seller_kindle_list[count])
        else:
            if writer_seller_kindle_list[count] == "Kindle Edition":
                kindle_list.append("Yes")
            else:
                kindle_list.append("No")
    return writer_list, seller_list, kindle_list


def book_badge(soup):
    tags = soup.select("span.a-icon-alt")
    star_list = [float(book.text.split(" ")[0]) for book in tags]
    return star_list


def main():
    url = "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&ref=lp_122131175011_sar"
    head = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
            "Accept-Encoding": "gzip, deflate, br", 
            "Accept": "*/*", 
            "Referer": "https://www.amazon.com/"}
    soup = requesting(url, head)
    # BookName = book_name(soup)
    # WriterSellerKindle = writer_seller_kindle(soup)
    # BookBadge = book_badge(soup)
    pprint(BookBadge)
    
main()