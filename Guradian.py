from bs4 import BeautifulSoup
import requests



root = 'https://www.theguardian.com/'
url = f'{root}/international'
result = requests.get(url)
content = result.text
soup = BeautifulSoup(content,'html.parser')


news_link =[]
for name in soup.find_all('a',href=True,class_= 'u-faux-block-link__overlay js-headline-text'):
    news_link.append(name['href'])

print(news_link)


for name in news_link:
    url = f'{root}/{name}'
    result = requests.get(url)
    content = result.text
    soup = BeautifulSoup(content, 'html.parser')
    print(name)

    #title
    title = []
    box =soup.find('a',class_='content__label__link dcr-yx39j8')
    title = box.find('span').text.strip()