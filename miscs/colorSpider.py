import urllib2
import json
from bs4 import BeautifulSoup

def fetchColors():
    resp = urllib2.urlopen('http://ylbook.com/cms/web/chuantongsecai/chuantongsecai.htm')
    src = resp.read()
    soup = BeautifulSoup(src)
    res = []
    for color in soup.findAll('dl'):
        values = color.findAll('span')
        meta = {
            'name': color.find(class_="colorName").text,
            'rgb': values[0].text,
            'cmyk': values[1].text,
            'hex': values[2].text,
            'desc': color.find(class_="colorDesc").text
        }
        res.append(meta)

    with open('colors.json', 'wb') as dst:
        json.dump(res, dst)

def main():
    fetchColors()

if __name__ == '__main__':
    main()