from HTMLParser import HTMLParser
import urlparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LinkFinder(HTMLParser):
    def __init__(self, baseUrl, pageUrl):
        HTMLParser.__init__(self)
        self.baseUrl=baseUrl
        self.pageUrl=pageUrl
        self.links = set()

    def handle_starttag(self,tag,attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = urlparse.urljoin(self.baseUrl,value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self,message):
        pass
