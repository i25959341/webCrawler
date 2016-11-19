from general import *
import threading
from Queue import Queue
from crawler import Spider
import sys
from config import *
reload(sys)
sys.setdefaultencoding('utf8')

threadQueue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

def createWorkers():
    for _ in range(NUMBER_OF_THREADS):
        t= threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = threadQueue.get()
        # print url + "hello"
        Spider.crawlPage(threading.current_thread().name, url)
        threadQueue.task_done()


def createJobs():
    for link in fileToSet(QUEUE_FILE):
        threadQueue.put(link)
    threadQueue.join()


def crawl():
    queueLinks = fileToSet(QUEUE_FILE)
    if len(queueLinks)>0:
        print str(len(queueLinks)) +" links in the quene"
        createJobs()

createWorkers()
while len(fileToSet(QUEUE_FILE)):
    crawl()
