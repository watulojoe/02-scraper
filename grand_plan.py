import pprint
import re

import requests
import bs4


def sn_page_url_formatter(url):
    """

    :param url:
    :return:
    """
    return re.compile(r'https://o2tvseries2.com/\S+/\S+/').search(url).group()


def get_elements(download_url):
    """

    :param download_url:
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(url=download_url, headers=headers)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    links_elem = soup.select("body > div > div.data_list a")
    return links_elem


def get_all_page_link(url, base_link, all_episodes_links, count):
    """

    :param url:
    :param base_link:
    :param all_episodes_links:
    :param count:
    :return:
    """
    the_links = get_elements(url)
    all_episodes_links += the_links
    # print(f"added {the_links}")
    # print(f"all episode links are {all_episodes_links}")
    if len(the_links) == 0:
        # print("done")
        return all_episodes_links
    else:
        url = base_link + "/page" + str(1 + count) + ".html"
        count += 1
        # print(f"done... going to {url}")
        get_all_page_link(url, base_link, all_episodes_links, count)
    return all_episodes_links


def ep_elem_list(url):
    """

    :param url:
    :return:
    """
    all_links = []
    count = 1
    base_link = url
    return get_all_page_link(url, base_link, all_links, count)


def final_episode_download_link(url):
    """

    :param url:
    :return:
    """
    elem = get_elements(url)
    return elem[1]["href"]
