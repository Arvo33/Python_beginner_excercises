from bs4 import BeautifulSoup

if __name__ == '__main__':
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; their names:
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    <b class="boldest">Extremely bold</b>
    <blockquote class="boldest">Extremely bold</blockquote>
    <b id="1">Test 1</b>
    <b another-attribute="1" id="verybold">Test 2</b>
    """

    with open('index.html', 'w') as f:
        f.write(html_doc)

    soup = BeautifulSoup(html_doc, 'html.parser')
    # print(soup.prettify())
    print(soup.b)   # only fist occurence
    print(soup.p)
    print(soup.find('p')) # only fist occurence
    print(soup.find_all('b'))   # all occurences
    print(soup.b.name)  # tag name

    print()
    tag = soup.b
    print(tag)
    tag.name = 'blackquote' # change tag name
    print(tag)

    # Attributes

    print()
    tag_2 = soup.find_all('b')[1]
    print(tag_2)
    print(tag_2['id'])

    print()
    tag_3 = soup.find_all('b')[2]
    print(tag_3)
    print(tag_3['id'])
    print(tag_3['another-attribute'])

    print()
    print(tag_3.attrs)  # all attributes

    print()
    tag_3['another-attribute'] = 2  # change attribute
    print(tag_3)

    print()
    del tag_3['id']     # deleting attribute
    print(tag_3)
    del tag_3['another-attribute']
    print(tag_3)

    print()
    print(tag_3.string)     # string
    print(tag_3.text)       # same output?

    print()
    tag_3.string.replace_with('This is another string')
    print(tag_3)
    print(tag_3.string)