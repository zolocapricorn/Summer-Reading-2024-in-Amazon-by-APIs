# Library Zone
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import re

class calling_url:
    def generate_url_amazon_page():
        """Single URL"""
        amazon_url = "https://www.amazon.com/s?i=digital-text&rh=n%3A23901427011&fs=true&page=1qid=1725787065&ref=sr_pg_1"
        amazon_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
                         "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
                         "Accept-Encoding": "gzip, deflate, br", 
                         "Accept": "*/*", 
                         "Referer": "https://www.amazon.com/"}
        return amazon_url, amazon_header
    
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
    

    def generate_url_each_of_book(soup):
        book_tag = soup.select("a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
        book_href_list = [tag.get("href") for tag in book_tag]
        book_link = "https://www.amazon.com/{0}"
        book_url = list(set([book_link.format(link) for link in book_href_list]))[0:3]
        return book_url
        

    # def generate_url_percentages_of_stars(soup, main_url):
    #     star_tag = soup.select("a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
    #     star_code_list = [tag.get("href").split("/")[3] for tag in star_tag][0::2]
    #     star_link = "https://www.amazon.com/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&asin={0}&ref_=acr_search__popover&contextId=search"
    #     star_url = [star_link.format(code) for code in star_code_list]
    #     star_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
    #                    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    #                    "Accept-Encoding": "gzip, deflate, br", 
    #                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    #                    "Referer": main_url}
    #     return star_url, star_header


    def requesting(url, header):
        if type(url) is list:
            response_list = []
            for each in url:
                response = requests.get(each, headers=header)
                if response.status_code == 200:
                    print(each)
                    print(response.status_code)
                    response_list.append(BeautifulSoup(response.text, "lxml"))
                    time.sleep(2.5)
                else:
                    return "Cannot requesting"
            return response_list
        else:
            response = requests.get(url, headers=header)
            if response.status_code == 200:
                return BeautifulSoup(response.text, "lxml")
            return "Cannot requesting"


class book:
    def __init__(self):
        # Main Calling
        self.MainURL, self.MainHeader = self.main_url_main_header()
        self.Soup = calling_url.requesting(self.MainURL, self.MainHeader)

    #     # Book Star Calling
    #     # self.StarURL, self.StarHeader = self.book_star_url_book_star_header()
    #     # self.Star = calling_url.requesting(self.StarURL, self.StarHeader)

        # Book Calling
        self.BookURL = self.book_url_book_header()
        self.Book = calling_url.requesting(self.BookURL, self.MainHeader)
    

    def main_url_main_header(self):
        MainURL, MainHeader = calling_url.generate_url_amazon_page()
        return MainURL, MainHeader
    

    def book_url_book_header(self):
        BookURL = calling_url.generate_url_each_of_book(self.Soup)
        return BookURL
    

    # def book_star_url_book_star_header(self):
    #     BookDetailURL, BookDetailHeader = calling_url.generate_url_percentages_of_stars(self.Soup, self.MainURL)
    #     return BookDetailURL, BookDetailHeader


    def book_name(self):
        tags = [books.select("span#productTitle") for books in self.Book]
        book_list = [book_name.text for book_tag in tags for book_name in book_tag]
        return book_list


    def writer_name(self):
        tags = [writers.select("span.author.notFaded > a") for writers in self.Book]
        writer_list = [writer_name.text for writer_tag in tags for writer_name in writer_tag]
        return writer_list
    

    def seller_name(self):
        tags = [sellers.select("td > span.a-color-base") for sellers in self.Book]
        seller_list = [seller_name.text for seller_tag in tags for seller_name in seller_tag]
        return seller_list
    

    def avaliable_kindle(self):
        tags = [kindle.select("span#productSubtitle") for kindle in self.Book]
        kindle_list = ["Yes" if kindle.text == "  Kindle Edition " else "No" for kindle_tag in tags for kindle in kindle_tag]
        return kindle_list
    

    # def users_review(self):
    #     tags = self.Soup
    
    
    # class book_stars:
    #     def __init__(self, book):
    #         self.BookStars = book


    #     def average_star(self):
    #         tags = self.BookStars.Star.select("span.a-icon-alt")
    #         average_star = [float(avg.text.split(" ")[0]) for avg in tags]
    #         return average_star


    #     def percentages_each_type_of_stars(self):
    #         five_star, four_star, three_star, two_star, one_star = [], [], [], [], []
    #         for taglist in self.BookStars.Star:
    #             tags = taglist.select("span")
    #             star_list = [data.text.replace(" ", "").replace("\n", "").replace("%", "") for data in tags if data.text.find("%") >= 0][1:6]
    #             five_star.append(star_list[0])
    #             four_star.append(star_list[1])
    #             three_star.append(star_list[2])
    #             two_star.append(star_list[3])
    #             one_star.append(star_list[4])
    #         return five_star, four_star, three_star, two_star, one_star


"""Single Calling"""
# Call 1st Class
# ClassCallingURL = calling_url()
ClassBook = book()

# Call 2nd Class
# SubClassBookStars = ClassBook.book_stars(ClassBook)

# Call Function
BookName = ClassBook.book_name()
WriterName = ClassBook.writer_name()
SellerName = ClassBook.seller_name()
KindleAvaliable = ClassBook.avaliable_kindle()
# WriterSellerKindle = ClassBook.writer_seller_kindle()
# AverageStars = SubClassBookStars.average_star()
# StarList = SubClassBookStars.percentages_each_type_of_stars()
# FiveStar, FourStar, ThreeStar, TwoStar, OneStar = SubClassBookStars.percentages_each_type_of_stars()
pprint(KindleAvaliable)

"""Note"""
# 1. BookName should to strip left and right
# 2. WriterName should check space between firstname and surname.
# 3. SellerName should to strip left and right

