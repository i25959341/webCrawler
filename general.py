import os
from urlparse import urlparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def createProject(dir):
    if not os.path.exists(dir):
        print 'Create dir' + dir
        os.makedirs(dir)

def createDateFiles(name, base):
    queue = os.path.join(name, 'queue.txt')
    crawled = os.path.join(name, 'crawled.txt')
    if not os.path.isfile(queue):
        writeFile(queue, base)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')

def writeFile(path,data):
    with open(path, 'w') as f:
        f.write(data)

def appendFile(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')

def deleteContent(path):
    open(path,'w').close()

def fileToSet(fileName):
    results=set()
    with open(fileName, 'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def setToFile(links, fileName):
    with open(fileName, 'w') as f:
        for l in sorted(links):
            f.write(l.encode('utf-8')+'\n')

def getDomainName(url):
    try:
        results = getSubDomainName(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
