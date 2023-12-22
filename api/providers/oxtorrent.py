import api.utils as utils
from bs4 import BeautifulSoup
import urllib.parse

def searchTorrents(query):
    soup = utils.getHtml("https://www.oxtorrents.co/recherche/films/" + query)

    content = soup.find("table", {"class": "table"})

    links = content.findAll("a")
    titles = [link.text for link in links]
    urls = ["https://www.oxtorrents.co" + link["href"] for link in links]
    
    descriptionsUrls = ["/view?source=" + urllib.parse.quote(url) for url in urls]

    result = []

    for i in range(len(titles)):
        result.append({"title": titles[i], "url": descriptionsUrls[i]})
        
    return result


def getMagnet(descriptionUrl):
    soup = utils.getHtml(descriptionUrl)

    buttonDiv = soup.find("div", {"class": "btn-magnet"})

    link = buttonDiv.find("a")
    magnet = link["href"]

    return magnet