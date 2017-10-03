from bs4 import BeautifulSoup as BS
import bs4
import urllib.request
import re

def getRSSSoup(symbol):
    """Returns a soup object for the RSS of a stocl symbol"""
    googleRSS = "https://finance.google.com/finance/company_news?q="+symbol+"&output=rss"
    r = urllib.request.urlopen(googleRSS).read()
    soup = BS(r,"lxml")
    return soup

def getLink(item):
    """Returns the link of an article from a soup item"""
    start=item.text.find('<a')
    end=item.text.find('" style')
    rawlink = item.text[start:end] + '"'
    link=rawlink.split('"')[1]
    return link

def getSite(link):
    """Returns the source site from a link"""
    site=link.split('/')[2]
    return site

def getRSSList(soup):
    """Returns a list of dictionaries with stock news information"""
    dictList = list()
    for index,item in enumerate(soup.findAll('item')):
        tempDict = dict()
        link = getLink(item)
        site = getSite(link)
        tempDict['source'] = site
        tempDict['date'] = item.find('pubdate').text
        tempDict['title'] = item.find('title').text
        tempDict['link'] = link
        dictList.append(tempDict)
    return dictList

def printRSSList(rssList):
    """Prints the list of news dictionaries"""
    for dic in rssList:
        for item in dic:
            print(item,' : ',dic[item])
        print('\n')

def getArticleText(url,aClass):
    """Returns the text of an article from a url"""
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent':user_agent}
    request=urllib.request.Request(url,None,headers)
    r = urllib.request.urlopen(request).read()
    soup = BS(r,"lxml")
    return soup.find('section',aClass).text

if __name__ == "__main__":
    soup = getRSSSoup('GOOGL')
    newsList = getRSSList(soup)
    # printRSSList(newsList)
    sourceClassDict = dict()
    sourceClassDict['fool'] = {"class":"usmf-new article-body"}
    for item in newsList:
        if item['source'] == 'www.fool.com':
            print('\n*****************************\n')
            print(getArticleText(item['link'],sourceClassDict['fool']))


    # motleyfool*
    # seekingalpha*
    # investorplace*
    # bloomberg*
    # pr newswire
    # marketwatch*
    # gurufocus
    # stocknewsjournal
    # reuters*
    # yahoofinance*
    # stocknews
    # ny stock news
    # amigo bulls
    # morgan research



    # foolSpliter = '<span class="article-content">'
    # r = urllib.request.urlopen(newsList[0]['link']).read()
    # soup = BS(r,"lxml")
    # for item in soup.findAll('section',{"class":"usmf-new article-body"}):
    #     print('\n*******************\n',item.text)
    # print(soup.prettify())
    # split =  r.split(foolSpliter)
    # print(split[1])

    # soup = BS(r,"lxml")
    # print(soup.prettify())
