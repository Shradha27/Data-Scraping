import requests
from bs4 import BeautifulSoup
import re
from bs4 import NavigableString


def crawler():
        url = 'https://innovate.mygov.in/sih2018-search'
        source_code = requests.get(url)
        text = source_code.text
        soup = BeautifulSoup(text, "html.parser")
        nos = []
        for div in soup.find_all(string=re.compile("Total Submissions")):
                txt = str(div)
                no = ""
                for i, c in enumerate(txt):
                        if i == 41 or i == 42 or i == 43:
                                no = no + c
                nos.append(int(no))
        for i in soup.findAll('div', {'class': 'head-part'}):
                if nos[i] < 10:
                    ts = i.next_sibling.div.get_text()
                    link = i.div.a.get('href')
                    title = i.div.a.string
                    print(title, link)

crawler()