# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York
# Times homepage.

from typing import List

import requests
from bs4 import BeautifulSoup


def get_article_titles(url: str) -> List[str]:
    src = requests.get(url).content
    soup = BeautifulSoup(src, 'html.parser').find_all('h2')
    article_titles = []
    title_class = 'esl82me0'
    for link in soup:
        if title_class in link['class']:
            article_titles.append(link.string)
    return article_titles


if __name__ == '__main__':
    my_url = 'https://www.nytimes.com/'

    titles = get_article_titles(my_url)
    for title in titles:
        print(title)
