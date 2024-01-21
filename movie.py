import pprint
import re

import requests
import bs4

# todo: do not update in this file



def url_formatter(url):
    """
    removes the extra generated code together with the index.html extension
    used in the scrapper() to format the links found in the given element
    :param url: "https://o2tvseries2.com/Archer-otv72f1z/index.html?codeo2=MmMwZjpmZTM4OjIyMGI6NjAwNDplOGMzOmM3NDE6NTc2Mzo3YzQuNTEyMw=="
    :return: https://o2tvseries2.com/Archer-otv72f1z/
    """
    return re.compile(r'https://o2tvseries2.com/\S+/').search(url).group()


def scraper(url):
    """
    downloads the webpage using requests and returns a response
    check the status using the raise for status function
    bs4 instance is made and the response obj is parsed as an argument
    all the a-tags in the css-selector(data-list) are selected and put in the dictionary box
    the box contains name as key and url as the value
    :param url: example - https://o2tvseries2.com/a
    :return: a dictionary which is the box
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    links_elem = soup.select("body > div > div.data_list a")
    box = {}
    for i in links_elem:
        name = i.get_text()
        url = url_formatter(i["href"])
        box.setdefault(name, url)
    # pprint.pprint(box)
    return box


links = {}
tvShowCount = 1


def get_series_links(lttr, my_url):
    # todo: update this code to be dynamic like episode_getter.py
    """
    for getting all the series links from the website https://o2tvseries.com
    url is passed in scrapper() and if len(link) is 0, it breaks from the recursion
    else links will be returned from the scrapper
    the links found will be updated in the variable links which is accessed locally
    url will be changed to go to the next-page-url
    the next-page-url will be passed in the function recursively and will stop when no links will be found(len = 0)

    :param lttr: y | v | s | p | m | j | g | d | a (either of the letters)
    :param my_url: "https://o2tvseries2.com/"
    my_url and lttr is concatenated before using this function
    :return: update the global var links by merging it with the new dict the_links
    """
    global links
    the_links = scraper(my_url)
    if len(the_links) == 0:
        return
    else:
        global tvShowCount
        links = links | the_links  # merging 2 dictionaries
        url = "https://o2tvseries2.com/" + lttr + "/page" + str(1 + tvShowCount) + ".html"
        tvShowCount += 1
        # print(f"done. moving to {url}...")
        get_series_links(lttr, url)


letter = "v"
the_url = "https://o2tvseries2.com/" + letter
get_series_links(letter, the_url)
print(links)
# pprint.pprint(links)
