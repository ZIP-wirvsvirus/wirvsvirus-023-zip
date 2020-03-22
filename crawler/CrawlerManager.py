from crawler.warnungBund import BundCrawler


class CrawlerManager:
    def __init__(self):
        self.crawler_list = []
        self.crawler_list.append(BundCrawler())

    def crawl_all(self, database):
        for crawler in self.crawler_list:
            try:
                crawler.collect_and_commit(database)
            except Exception as ex:
                print(ex)
