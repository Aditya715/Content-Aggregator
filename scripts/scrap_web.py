"""
    This file will go up on the internet and scrap the data kept over there
    and save it to a database for further use.
"""

import sys
from datetime import (
    datetime, 
    timedelta
)
import requests
from bs4 import BeautifulSoup as bs
from content.models import (
    RealStateNews,
    RealStateArticle
)

def scrap_data(url, num_of_pages_to_crwal):

    list_of_data = [] 

    if num_of_pages_to_crwal > 200:
        print("[+]---> Page limit = 200")
        num_of_pages_to_crwal = 200
    
    for i in range(1,num_of_pages_to_crwal+1):
        if i == 1:
            new_url = url
        else:
            new_url = url + "/page/" + str(i)

        print("[+]----> Crawling {}".format(new_url))
        # getting data using python requests
        response = requests.get(new_url, timeout=20)
        # reponse status_code filter here
        if response.status_code == 200:
            soup = bs(response.text, "lxml")
            # data filtering starts here...
            banners = soup.find_all("div", class_="kc_bannertxt")
            try:
                # iterating over each one to get data in a list
                for count,banner in enumerate(banners):
                    hrefs = banner.find_all("a")
                    if count == 0:
                        date_of_publish = banner.find("span", class_="date")
                    else:
                        date_of_publish = banner.find_all("span")[-2].find("em")
                    temp = {}
                    if len(hrefs) == 3:
                        temp = {
                            'title' : hrefs[1].text,
                            'url' : hrefs[1].get("href"),
                            'author' : hrefs[2].text,
                            'date' : datetime.strptime(date_of_publish.text, '%b %d, %Y').date()
                        }
                    elif len(hrefs) == 2:
                        temp = {
                            'title' : hrefs[0].text,
                            'url' : hrefs[0].get("href"),
                            'author' : hrefs[1].text,
                            'date' : datetime.strptime(date_of_publish.text, '%b %d, %Y').date()
                        }
                    if temp:
                        list_of_data.append(temp)
            except Exception as e:
                print(f"Error occured {e}")
    
    return list_of_data


def scrap_99acres():
    """
        This function is made to get relevant data from 99 acres website.
    """
    news_url = "https://www.99acres.com/articles/real-estate-news"
    articles_url = "https://www.99acres.com/articles/real-estate-market-updates.html"
    num_of_pages_to_crwal = 20       # max value is 200.

    news_list = scrap_data(news_url, num_of_pages_to_crwal)
    articles_list = scrap_data(articles_url, num_of_pages_to_crwal)
    
    for news in news_list:
        # handling database error
        try:
            RealStateNews(**news).save()
        except Exception as e:
            print("[+]....Error occured -> {}".format(e))
    
    for article in articles_list:
        # handling database error
        try:
            RealStateArticle(**article).save()
        except Exception as e:
            print("[+]....Error occured -> {}".format(e))


def run():
    while True:
        now = datetime.now()
        if now.hour == 1 and now.minute <= 10:
            scrap_99acres()
            time.sleep(60*60)
        else:
            current_date = datetime.today().date()
            next_date = str(current_date + timedelta(days=1))
            run_time = datetime.strptime(next_date + " 01:00:00", '%Y-%m-%d %H:%M:%S')
            current_time = datetime.now()
            difference = run_time - current_time
            sys.stdout.write("Time left to run scripts for data : " + str(difference) + "\r")
            sys.stdout.flush()