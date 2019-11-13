import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    src = requests.get('https://www.whitehouse.gov/briefings-statements/').content
    soup = BeautifulSoup(src, 'html.parser')
    h2_tags = soup.find_all('h2')

    urls = []
    for h2_tag in h2_tags:
        a_tag = h2_tag.find('a')
        urls.append(a_tag.attrs['href'])

    print(urls)
