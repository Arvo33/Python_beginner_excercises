import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    result = requests.get('https://www.google.com')
    print(result.status_code)
    # print(result.headers)
    src = result.content
    # print(src)
    soup = BeautifulSoup(src)
    links = soup.find_all("a")
    # print(links)
    # print()

    for link in links:
        if "Wszystko" in link.text:
            print(link)
            print(link.attrs['href'])
