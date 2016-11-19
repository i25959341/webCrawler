# webCrawler

To get started, edit the parameters in the config.py, like the website you would like to crawl and number threads to use

- python main.py

# Requirements for the assignment

- Create a site map for a given url
- Extract static assets from each url in the created site map

# Design Decisions:

The design need to be based on robustness, performance, testing, and code structure & layout. Multi-threading is used for the crawler to run faster.

# Future plan

- Need to have unit testing
- Have offline file for crawled assets like queue.txt and crawl.txt
- there is an issue that the webcrawler would stop after sometimes, I think there might some concurrency issue with the code (Consumer Producer problems)

# Features

- Multithreading for faster performance
- Generates xml sitemap showing pages and assets
- Offline storing the crawled links, so if anything happens, have backup files to crawl again

# References

- https://github.com/samistart/WebCrawler
- https://www.youtube.com/watch?v=nRW90GASSXE&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0q



