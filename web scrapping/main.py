import requests
from bs4 import BeautifulSoup
import pprint


def fun(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select(".storylink")
    subtext = soup.select('.subtext')

    def custom_news(links, subtext):
        hn = []
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href')
            vote = subtext[idx].select('.score')
            if (len(vote)):
                points = (vote[0].getText().replace(' points', ''))
                points = int(points.replace(' point', ''))
                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sorted(hn, key=lambda k: k['votes'])

    g = custom_news(links, subtext)
    pprint.pprint(g[::-1])


n = input("enter the no of pages \n")
j = f"https://news.ycombinator.com/news?p={n}"
res = requests.get(j)
fun(res)
