# Library Zone
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time

class calling_url:
    def generate_url_amazon_page():
        """Single URL"""
        url = "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&page=1&qid=1725787065&ref=sr_pg_1"
        header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
                  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
                  "Accept-Encoding": "gzip, deflate, br", 
                  "Accept": "*/*"}
        return url, header
    
        """Multiple URL"""
        # url_list = []
        # url = "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&page={0}&qid=1725787065&ref=sr_pg_{1}"
        # header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
        #          "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
        #          "Accept-Encoding": "gzip, deflate, br", 
        #          "Accept": "*/*"}
        # for page in range(1, 9):
        #     if page == 1:
        #         url_list.append((url.format(page, page), header))
        #     else:
        #         url_list.append((url.format(page, page-1), header))
        # return url_list
    

    def generate_url_percentages_each_type_of_stars(soup):
        book_link = soup.select("a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal[href]")
        book_code_list = [link.split("/")[2] for link in book_link]
        return book_code_list


    def requesting(url, header):
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "lxml")
        return "Cannot requesting"


class book_detail:
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


    def total_star(soup):
        tags = soup.select("span.a-icon-alt")
        star_list = [float(book.text.split(" ")[0]) for book in tags]
        return star_list


    class stars:
        def __init__(self):
            self.start = "https://www.amazon.com/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&asin="
            self.end = "&ref_=acr_search__popover&contextId=search"
            self.header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
                           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
                           "Accept-Encoding": "gzip, deflate, br", 
                           "Accept": "text/html,*/*"}


        def percentages_each_type_of_stars(self):
            tags = self.soup.select("a-fixed-left-grid")
            return tags
            # five_star_list = [book.text for book in tags]


def main():
    """Single Calling"""
    url, header = calling_url.generate_url_amazon_page()
    soup = calling_url.requesting(url, header)
    # BookName = book_name(soup)
    # WriterSellerKindle = writer_seller_kindle(soup)
    # TotalStars = total_stars(soup)
    URLPercentageEachTypeOfStars = calling_url.generate_url_percentages_each_type_of_stars(soup)
    pprint(URLPercentageEachTypeOfStars)

    """Multiple Calling"""
    # for url, header in URLHeader:
        # soup = calling_url.requesting(url, header)
        # BookName = book_name(soup)
        # WriterSellerKindle = writer_seller_kindle(soup)
        # TotalStars = total_stars(soup)
        # URLPercentageEachTypeOfStars = calling_url.generate_url_percentages_each_type_of_stars(soup)
        # BookStar = book_stars(soup)
        # pprint(URLPercentageEachTypeOfStars)
        # time.sleep(5)
    
main()