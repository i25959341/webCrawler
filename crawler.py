from urllib2 import urlopen
from linkFinder import LinkFinder
from xmlWriter import XmlWriter
from urlparse import urljoin

import bs4
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from general import *

class Spider:
    projectName=''
    baseUrl = ''
    domainName = ''
    queueFile = ''
    crawledFile = ''
    queue = set()
    crawled = set()
    xml_writer = None
    assets=set()

    def __init__(self, projectName, baseUrl, domainName):
        Spider.projectName = projectName
        Spider.baseUrl = baseUrl
        Spider.domainName = domainName
        Spider.queueFile = Spider.projectName + '/queue.txt'
        Spider.crawledFile = Spider.projectName + '/crawled.txt'
        if Spider.xml_writer is None:
            Spider.xml_writer = XmlWriter()
        self.boot()
        self.crawlPage('First spider', Spider.baseUrl)


    @staticmethod
    def boot():
        createProject(Spider.projectName)
        createDateFiles(Spider.projectName, Spider.baseUrl)
        Spider.queue = fileToSet(Spider.queueFile)
        Spider.crawled = fileToSet(Spider.crawledFile)

    @staticmethod
    def crawlPage(threadName, pageUrl):
        # print Spider.crawled
        if pageUrl not in Spider.crawled:
            print threadName + ' crawling ' + pageUrl
            print 'Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(
            Spider.crawled))
            Spider.addLinks(Spider.gatherLinks(pageUrl))
            Spider.queue.remove(pageUrl)
            Spider.crawled.add(pageUrl)
            Spider.updateFiles()

    @staticmethod
    def gatherLinks(pageUrl):
        html=''
        url_info = urlparse(pageUrl)
        try:
            # print pageUrl
            response = urlopen(pageUrl)
            if 'text/html' in response.info().getheader('Content-Type'):
                path = url_info.path
                Spider.xml_writer.write(path)
                htmlBytes = response.read()
                html = htmlBytes.decode("utf-8")
                soup = bs4.BeautifulSoup(htmlBytes, "html.parser")
                Spider.getAssets(soup)
            finder=LinkFinder(Spider.baseUrl, pageUrl)
            finder.feed(html)
        except Exception as e:
            print str(e)
            return set()
        return finder.page_links()

    @staticmethod
    def getAssets(soup):
        for asset in [i.get('src') for i in soup.find_all() if i.get('src')]:
            url_info = urlparse(asset)
            if url_info.netloc == '' or url_info.netloc == Spider.domainName:
                path = url_info.path
                url = urljoin(Spider.baseUrl,path)
                if url not in Spider.assets:
                    Spider.xml_writer.write(path)
                Spider.assets.add(path)

    @staticmethod
    def addLinks(links):
        for url in links:
            if url in Spider.queue or url in Spider.crawled:
                continue
            if Spider.domainName != getDomainName(url):
                continue
            Spider.queue.add(url)

    @staticmethod
    def updateFiles():
        setToFile(Spider.queue, Spider.queueFile)
        setToFile(Spider.crawled, Spider.crawledFile)
