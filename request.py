# Library Zone
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time
import re

class calling_url:
    def generate_url_amazon_page():
        """Single URL"""
        amazon_url = "https://www.amazon.com/s?i=digital-text&rh=n%3A122131175011&fs=true&page=1qid=1725787065&ref=sr_pg_1"
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
    

    def generate_url_percentages_of_stars(soup, main_url):
        """Single Generate"""
        book_link = soup.select("a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
        book_code_list = [link.get("href").split("/")[3] for link in book_link][0::2]
        book_star_url = "https://www.amazon.com/review/widgets/average-customer-review/popover/ref=acr_search__popover?ie=UTF8&asin={0}&ref_=acr_search__popover&contextId=search"
        book_url = [book_star_url.format(code) for code in book_code_list]
        book_header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15", 
                       "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
                       "Accept-Encoding": "gzip, deflate, br", 
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                       "Referer": main_url}
        return book_url, book_header


    def requesting(url, header):
        if type(url) is list:
            response_list = []
            for each in url:
                response = requests.get(each, headers=header)
                if response.status_code == 200:
                    response_list.append(BeautifulSoup(response.text, "lxml"))
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
        self.MainURL, self.MainHeader = self.main_url_main_header()
        self.Soup = calling_url.requesting(self.MainURL, self.MainHeader)
        self.BookDetailURL, self.BookDetailHeader = self.book_url_book_header()
        self.Book = calling_url.requesting(self.BookDetailURL, self.BookDetailHeader)
    

    def main_url_main_header(self):
        MainURL, MainHeader = calling_url.generate_url_amazon_page()
        return MainURL, MainHeader
    

    def book_url_book_header(self):
        BookDetailURL, BookDetailHeader = calling_url.generate_url_percentages_of_stars(self.Soup, self.MainURL)
        return BookDetailURL, BookDetailHeader


    def book_name(self):
        tags = self.Soup.select("span.a-size-medium")
        book_list = [book.text for book in tags]
        return book_list


    def writer_seller_kindle(self):
        tags = self.Soup.select("a.a-size-base")
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
    

    # def users_review(self):
    #     tags = self.Soup
    
    
    class book_stars:
        def __init__(self, book):
            self.BookStars = book


        def average_star(self):
            tags = self.BookStars.Soup.select("span.a-icon-alt")
            average_star = [float(avg.text.split(" ")[0]) for avg in tags]
            return average_star


        def percentages_each_type_of_stars(self):
            five_star, four_star, three_star, two_star, one_star = [], [], [], [], []
            for taglist in self.BookStars.Book:
                tags = taglist.select("span")
                star_list = [data.text.replace(" ", "").replace("\n", "").replace("%", "") for data in tags if data.text.find("%") >= 0][1:6]
                five_star.append(star_list[0])
                four_star.append(star_list[1])
                three_star.append(star_list[2])
                two_star.append(star_list[3])
                one_star.append(star_list[4])
            return five_star, four_star, three_star, two_star, one_star


"""Single Calling"""
# Call 1st Class
# ClassCallingURL = calling_url()
ClassBook = book()

# Call 2nd Class
SubClassBookStars = ClassBook.book_stars(ClassBook)

# Call Function
# BookName = ClassBook.book_name()
# WriterSellerKindle = ClassBook.writer_seller_kindle()
# AverageStars = SubClassBookStars.average_star()
# StarList = SubClassBookStars.percentages_each_type_of_stars()
FiveStar, FourStar, ThreeStar, TwoStar, OneStar = SubClassBookStars.percentages_each_type_of_stars()
print(FiveStar, FourStar, ThreeStar, TwoStar, OneStar)


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

